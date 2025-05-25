
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

df = pd.read_csv(HPIfile)
print(df.head(1000))

df['AreaCode'] = df['AreaCode'].str.replace(r'[a-zA-Z]', '', regex=True)
#df['AreaCode'] = pd.to_numeric(df['AreaCode'], errors='coerce')

df.replace(["", " ", "NA", "N/A", "?"], np.nan, inplace=True)
#  specify columns to impute ===
cols_to_impute  = ['CashIndex', 'MortgageIndex', 'AveragePrice','Index','IndexSA','1m%Change','12m%Change','AveragePriceSA','SalesVolume','DetachedPrice','DetachedIndex','Detached1m%Change','Detached12m%Change','NewPrice','NewIndex','New1m%Change','New12m%Change','NewSalesVolume','OldPrice','OldIndex','Old1m%Change','Old12m%Change','SemiDetachedPrice','SemiDetachedIndex','SemiDetached1m%Change','SemiDetached12m%Change','TerracedPrice','TerracedIndex','Terraced1m%Change','Terraced12m%Change','FlatPrice','FlatIndex','Flat1m%Change','Flat12m%Change']

# Convert columns to numeric if necessary
df[cols_to_impute] = df[cols_to_impute].apply(pd.to_numeric, errors='coerce')

# === Apply MICE (IterativeImputer) ===
imputer = IterativeImputer(random_state=0)
imputed_values = imputer.fit_transform(df[cols_to_impute])


# === Replace original columns with imputed results ===
df[cols_to_impute] = imputed_values

df.to_csv("Data/Silver//HPI/UK-HPI_Imputed_MICE-2025-02.csv", index=False)



