import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer
import logging
import time

from Utility.DownloadData import download_file_if_needed

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
    filename='Data/Silver/HPI/Mice.log',  # Output log file (optional)
    filemode='a'  # Append to file, use 'w' to overwrite
)

HPIfile = "Data/Bronze/HPI/HousePriceIndex.csv"
start_time = time.time()  # Record start time


logging.warning("Start")

logging.info("Download to Bronze")
download_file_if_needed(
    url="https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2025-03.csv",
    dest_path=HPIfile
)

logging.info("Read")
df = pd.read_csv(HPIfile)
print(df.head(1000))

logging.info("Clense")
df['AreaCode'] = df['AreaCode'].str.replace(r'[a-zA-Z]', '', regex=True)


df.replace(["", " ", "NA", "N/A", "?"], np.nan, inplace=True)
#  specify columns to impute ===
cols_to_impute  = ['CashIndex', 'MortgageIndex', 'AveragePrice','Index','IndexSA','1m%Change','12m%Change','AveragePriceSA','SalesVolume','DetachedPrice','DetachedIndex','Detached1m%Change','Detached12m%Change','NewPrice','NewIndex','New1m%Change','New12m%Change','NewSalesVolume','OldPrice','OldIndex','Old1m%Change','Old12m%Change','SemiDetachedPrice','SemiDetachedIndex','SemiDetached1m%Change','SemiDetached12m%Change','TerracedPrice','TerracedIndex','Terraced1m%Change','Terraced12m%Change','FlatPrice','FlatIndex','Flat1m%Change','Flat12m%Change']

# Convert columns to numeric if necessary
df[cols_to_impute] = df[cols_to_impute].apply(pd.to_numeric, errors='coerce')

logging.info("Transform")
# === Apply MICE (IterativeImputer) ===
imputer = IterativeImputer(random_state=0)
imputed_values = imputer.fit_transform(df[cols_to_impute])

logging.info("Impute")
# === Replace original columns with imputed results ===
df[cols_to_impute] = imputed_values

logging.info("Save")
df.to_csv("Data/Silver//HPI/UK-HPI_Imputed_MICE-2025-02.csv", index=False)

end_time = time.time()  # Record end time
time_taken = end_time - start_time


logging.warn(f"Finished: {time_taken:.4f} seconds")



