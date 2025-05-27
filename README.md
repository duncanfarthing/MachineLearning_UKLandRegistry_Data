# Property Data Imputation with MICE & Random Forest

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Source](https://img.shields.io/badge/Data-UK%20Land%20Registry-orange)](https://landregistry.data.gov.uk/app/ukhpi)

---

## Overview

This project explores advanced imputation and prediction techniques using **MICE (Multiple Imputation by Chained Equations)** and **Random Forests**, applied to the **UK Land Registry’s House Price Index (HPI)** dataset.

The dataset contains real-world gaps — such as missing data for specific property types in certain geographic areas. These gaps prevent accurate regional comparisons and national index generation. Our aim is to:

- Predict missing house price values and indices
- Enable consistent comparison across **property types** and **regions**
- Forecast price trends in underserved or emerging housing markets

---

## Architecture

The project uses a **Medallion Architecture** pattern:

- **Bronze**: Raw HPI data from UK Land Registry
- **Silver**: Cleaned and standardized data
- **Gold**: Imputed and enriched data, ready for analysis and forecasting

>  This structure prepares the data for easy transition into a **lakehouse** setup, if needed.

---

##  Methods & Tools

- **MICE** for chained imputations of missing values
- **Random Forest** for trend-based prediction
- **Macroeconomic enrichment** with:
  - GDP
  - Interest rates
  - Mortgage rates  
  (joined by month/year to support more realistic predictions)

---

##  Planned Features

- [ ]  Implement Random Forest model to:
  - Predict future HPI values based on trends
  - Simulate "what-if" scenarios
- [ ]  Join and align macroeconomic indicators with HPI data
- [ ]  Add visualizations (geospatial and temporal)
- [ ]  Evaluate performance using cross-validation and MAPE/RMSE

---

##  Getting Started

###  Requirements

- Python 3.9+
- pandas, numpy
- scikit-learn
- fancyimpute or miceforest
- matplotlib, seaborn (optional for visualization)

### ▶ Quick Start

```bash
git clone https://github.com/yourusername/property-imputation-project.git
cd property-imputation-project
pip install -r requirements.txt
python notebooks/imputation_workflow.py






