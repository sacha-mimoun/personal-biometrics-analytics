# 📊 Personal Biometrics Analytics

**Time-series analytics** on biometric signals (**HRV, resting heart rate, sleep efficiency, glucose variability**) using **Python, Pandas, Prophet, and machine learning**.  
Includes **exploratory data analysis (EDA)**, **feature engineering**, and **forecasting baselines**.

> ⚠️ All data in `data/` is **synthetic**, generated for demonstration purposes.  
> No personal or medical data is used.

---

## 🚀 Features
- **Synthetic biometric dataset** from July 2023 to July 2025
- **Daily HRV, resting heart rate, sleep efficiency, glucose variability**
- Exploratory visualizations (**Matplotlib**, **Seaborn**)
- Statistical baselines (**ARIMA**, **Prophet**, **Random Forest**)
- Trend detection and seasonality decomposition
- Forecasting future biometric metrics

---

## 📂 Project Structure                                                                             personal-biometrics-analytics/
│── data/                       # Synthetic biometric data
│── notebooks/                  # Jupyter notebooks for EDA & modeling
│   └── 01_EDA.ipynb
│── outputs/                    # Generated plots & reports
│── scripts/                    # Utility scripts
│   └── generate_biometrics.py
│── src/                        # Core analytics code
│── requirements.txt            # Python dependencies
│── .gitignore                  # Ignore cache & env files
└── README.md                   # Documentation                                                     ---

## 🔧 Installation
```bash
git clone https://github.com/sacha-mimoun/personal-biometrics-analytics.git
cd personal-biometrics-analytics
pip install -r requirements.txt
python3 scripts/generate_biometrics.py \
    --start 2023-07-01 --end 2025-07-31 \
    --out data/biometrics.csv --seed 42                                                             jupyter notebook notebooks/01_EDA.ipynb                                       
Example Output

HRV and Resting Heart Rate over time
Sleep Efficiency Distribution
📈 Potential Extensions
	•	Add continuous glucose monitoring (CGM) simulation
	•	Correlate biometric data with physical activity logs
	•	Integrate wearable device APIs (e.g., Oura, Whoop, Apple Health)

⸻

📜 License

MIT License – feel free to use and adapt.
