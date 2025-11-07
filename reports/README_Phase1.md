# 🛰️ ALLANAI.CrimeVision — Phase 1 Report (Oct – Dec 2022)

**Author:** Mahira  
**Organization:** ALLANAI Labs  
**Data Source:** [UK Police API](https://data.police.uk/api/)  
**License:** Open Government License v3.0  

---

## 1️⃣ Overview
This is **Phase 1** of the ALLANAI.CrimeVision initiative — an open-data project that collects and analyzes crime statistics across the UK to build transparent, AI-ready datasets.  
This phase covers three months (**October – December 2022**) and five major police forces.

---

## 2️⃣ Data Coverage
| Police Force | Region |
|---------------|---------|
| Metropolitan Police | London |
| Greater Manchester Police | Manchester |
| West Midlands Police | Birmingham |
| West Yorkshire Police | Leeds |
| Thames Valley Police | Oxford Region |

---

## 3️⃣ Dataset Details
| File | Description |
|------|--------------|
| `data_uk_2022_10/` | Raw monthly CSV files for October 2022 |
| `data_uk_2022_11/` | Raw monthly CSV files for November 2022 |
| `data_uk_2022_12/` | Raw monthly CSV files for December 2022 |
| `merged/UK_Crime_Oct_Dec_2022.csv` | Clean combined dataset used for Kaggle release |
| `notebooks/01_EDA_UK_Crime_Oct_Dec_2022.ipynb` | Exploratory Data Analysis notebook |

---

## 4️⃣ Data Schema
| Column | Description |
|---------|--------------|
| `crime_id` | Unique identifier for each crime record |
| `crime_type` | Type or category of crime |
| `month` | Month of report (YYYY-MM) |
| `latitude` / `longitude` | Incident location |
| `street_name` | Reported street name |
| `outcome` | Investigation status |
| `force_id` | Police force code |
| `neighbourhood_id` | Local neighbourhood code |

---

## 5️⃣ Data Collection Process
1. Queried the [UK Police API](https://data.police.uk/api/) for each force’s neighbourhoods.  
2. Extracted latitude/longitude centroids to avoid over-long polygon URLs.  
3. Retrieved crime data for each month via `/crimes-street/all-crime`.  
4. Normalized JSON to tabular form and merged across forces.  
5. Deduplicated by `crime_id` and validated columns.  
6. Saved final merged dataset in `merged/` folder.

---

## 6️⃣ Key Insights (from EDA)
- **Anti-social behaviour** and **violence and sexual offences** were the most frequent categories.  
- **Metropolitan Police area** recorded the highest incident density.  
- Seasonally, December showed slightly lower activity, possibly due to reporting lags.

---

## 7️⃣ Next Steps
| Phase | Timeline | Description |
|--------|-----------|--------------|
| Phase 2 | 2023 Q1 | Add Jan–Mar 2023 data |
| Phase 3 | 2023 Q2 | Integrate population + weather context |
| Phase 4 | 2024–25 | Build AI models for crime prediction |

---

## 8️⃣ References
- [UK Police Data API Documentation](https://data.police.uk/docs/)  
- Home Office Open Data Strategy (2022)  

---

💡 **Project Lead:** Mahira Banu  
🌐 **Organization:** [ALLANAI Labs](https://github.com/allanai-labs)  
📧 **Contact:** letsconnect@mahirabanu.com  
