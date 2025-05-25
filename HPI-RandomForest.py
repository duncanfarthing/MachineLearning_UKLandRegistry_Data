import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from Utility.DownloadData import download_file_if_needed
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of log messages
    filename='Data/Silver/HPI/RandowmForest.log',  # Output log file (optional)
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

#convert area code to numeric
df['AreaCode'] = df['AreaCode'].str.replace(r'[a-zA-Z]', '', regex=True)

logging.info("Transform")
df.replace(["", " ", "NA", "N/A", "?"], np.nan, inplace=True)

target = 'CashPrice' #column to predicted
#columns(features) to be used in prediction
features  = ['AreaCode','CashIndex', 'MortgageIndex', 'AveragePrice','Index','IndexSA','1m%Change','12m%Change','AveragePriceSA','SalesVolume','DetachedPrice','Detached1m%Change','Detached12m%Change','NewPrice','NewIndex','New1m%Change','New12m%Change','NewSalesVolume','OldPrice','OldIndex','Old1m%Change','Old12m%Change', 'MortgagePrice']

known = df[df[target].notnull()]
unknown = df[df[target].isnull()]

logging.info("Train")
model = RandomForestRegressor(random_state=42)
model.fit(known[features], known[target])

# Convert columns to numeric if necessary
#df[cols_to_impute] = df[cols_to_impute].apply(pd.to_numeric, errors='coerce')
logging.info("Predict")
df['CashPrice_imputed'] = df['CashPrice']  # start with original

logging.info("Impute")
df.loc[df['CashPrice'].isnull(), 'CashPrice_imputed'] = model.predict(unknown[features])

# === Save result to Silver ===
logging.info("Save")
df.to_csv("Data/Silver/HPI/UK-HPI_Imputed_RandomForest-2025-02.csv", index=False)

end_time = time.time()  # Record end time
time_taken = end_time - start_time


logging.warn(f"Finished: {time_taken:.4f} seconds")