from data_downloader import download_data
from smartmoneyconcepts.smc import smc
import pandas as pd

instrument = "NSE_INDEX|Nifty 50"
start_date = "2024-08-01"
end_date = "2024-09-10"
interval = "1minute"

data = download_data(instrument, start_date, end_date, interval)
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

swing_highs_lows_data = smc.swing_highs_lows(df, swing_length=5)

bos_choch_data = smc.bos_choch(df, swing_highs_lows_data)

# Print the first 5 rows of the DataFrame
filtered_df = bos_choch_data[bos_choch_data[['BOS', 'CHOCH', 'Level', 'BrokenIndex']].notna().any(axis=1)]

print(filtered_df)