
from Utility.DownloadData import download_file_if_needed
import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer


HPIfile = "Data/Bronze/HPI/HousePriceIndex.csv"

download_file_if_needed(
    url="https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2025-03.csv",
    dest_path=HPIfile
)

df = pd.read_csv(HPIfile,nrows=100)
print(df.head(10))





