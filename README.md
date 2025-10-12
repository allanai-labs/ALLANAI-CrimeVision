# 🛰️ ALLANAI-CrimeVision

**ALLANAI-CrimeVision** is an AI-powered public safety and crime data analysis module under the [ALLANAI SKY ecosystem](https://github.com/allanai-labs).  
This open-source project leverages UK crime datasets to identify patterns, visualize hotspots, and lay the foundation for predictive public safety systems.

> 📊 "Turning raw data into safety insights for smarter communities."

---

## 🚀 Features

- 🔗 Fetch real UK Police API crime data
- 🧹 Clean and structure raw data for analysis
- 📍 Focus: London region (Jan 2023 onward)
- 📈 Supports EDA, ML model training, and visualization
- 🔮 Designed for public safety innovation and civic tech

---

## 📁 Project Structure

```bash
ALLANAI-CrimeVision/
├── data/
│   └── raw/                  # Raw CSVs from UK Police API
├── notebooks/                # Jupyter notebooks for EDA, ML, reports
├── reports/                  # Visual summaries and writeups
├── src/                      # Python scripts for automation
│   ├── fetch_crime_data.py       # Fetches and saves monthly crime data
│   ├── data_loader.py            # Prepares clean DataFrames
│   ├── analysis.py               # Functions for exploring crime data
│   └── visualization.py          # Charts, maps, graphs
├── LICENSE
├── README.md
└── requirements.txt

🧑‍💻 Getting Started

Install dependencies

    pip install -r requirements.txt


Run the data fetch script

    python src/fetch_crime_data.py


Your data will be saved to:

    data/raw/london_crime_2023-01.csv


You can change the month or coordinates in the script for other cities or dates.

🔍 Data Source

 - 📡 Source: UK Police Data API

 - 🗺️ Region: Greater London (default)

 - 📅 Time: Monthly basis (e.g., Jan 2023)

 - 🧾 Fields: Category, location, outcome, time, coordinates

🧩 Use Cases

📌 Map crime hotspots for awareness

📉 Study crime trends and drop rates

🧠 Feed structured data into ML models

📍 Build smart dashboards or reports

⚖️ Support civic transparency and open data movements

📌 Roadmap

✅ Setup project and folder structure

✅ Fetch and store initial London dataset

⏳ Data cleaning and EDA (next step)

🔮 Visualizations: bar plots, heatmaps, maps

🧠 Machine Learning (classification, clustering)

📊 Kaggle Dataset and Notebook uploads

♻️ Monthly automation with cron or GitHub Actions

📄 License

Licensed under the MIT License
→ Free to use, modify, share, or contribute (with credit)

👩‍💻 Author

Mahira Banu
📧 letsconnect@mahirabanu.com

🌍 mahirabanu.com

🐙 GitHub: @mahirabanu

📊 Kaggle: @mahirabanu

🇬🇧 MSc Data Science | UK | Global Talent Visa (Tech Nation) Aspirant

🤝 Contributing

    We welcome contributions!

    💡 Suggest ideas in Issues

    🛠️ Fork and submit PRs

    📣 Share with civic-tech and open-data communities

💡 Inspiration

ALLANAI-CrimeVision is part of the ALLANAI SKY innovation suite — a set of AI tools for aviation, public safety, and sustainability.
This module specifically explores how data can help predict, prevent, and better understand crime trends for public benefit.

⭐ Show Some Love

If you like this project:

    ⭐ Star this repo

    📢 Share it on LinkedIn / Twitter

    💬 Give feedback on Kaggle or GitHub

Together, let’s build a safer, data-driven future 🚨📊🌍