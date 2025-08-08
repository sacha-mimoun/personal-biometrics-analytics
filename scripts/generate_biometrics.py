import argparse
import numpy as np
import pandas as pd

def clip(a, lo, hi):
    return np.minimum(np.maximum(a, lo), hi)

def main(start, end, out_path, seed):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start, end=end, freq="D")
    n = len(dates)

    doy = dates.dayofyear.values
    dow = dates.weekday.values  # 0=Mon ... 6=Sun
    weekend = (dow >= 5).astype(float)
    year_season = np.sin(2*np.pi * (doy/365.25))  # saisonnalité annuelle [-1,1]
    week_season = np.sin(2*np.pi * (dow/7))       # pattern hebdo

    # HRV (ms): base ~60, monte légèrement l'été, mieux le week-end
    hrv_base = 60 + 4*year_season + 2*weekend
    hrv_noise = rng.normal(0, 3, size=n)
    hrv = clip(hrv_base + hrv_noise, 30, 110)

    # Resting HR (bpm): inversement corrélé à HRV + bruit
    rhr_base = 58 - 0.18*(hrv - 60)
    rhr_noise = rng.normal(0, 2.2, size=n)
    resting_hr = clip(rhr_base + rhr_noise, 45, 85)

    # Sleep efficiency (0-1): meilleur le week-end + légère saisonnalité
    sleep_base = 0.90 + 0.02*weekend + 0.01*year_season
    sleep_noise = rng.normal(0, 0.03, size=n)
    sleep_eff = clip(sleep_base + sleep_noise, 0.75, 0.99)

    # Glucose variability (mg/dL): augmente si sommeil mauvais & RHR haut, baisse avec HRV haut
    gv = (12
          + 0.06*(resting_hr - resting_hr.mean())
          - 0.05*(hrv - hrv.mean())
          + 3.0*(1 - sleep_eff)
          + rng.normal(0, 1.5, size=n))
    glucose_var = clip(gv, 6, 25)

    df = pd.DataFrame({
        "date": dates,
        "hrv": np.round(hrv, 1),
        "resting_hr": np.round(resting_hr, 0).astype(int),
        "sleep_efficiency": np.round(sleep_eff, 3),
        "glucose_variability": np.round(glucose_var, 1),
    })

    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path} ({df['date'].min().date()} → {df['date'].max().date()})")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--start", required=True)
    p.add_argument("--end", required=True)
    p.add_argument("--out", default="data/biometrics.csv")
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()
    main(args.start, args.end, args.out, args.seed)
