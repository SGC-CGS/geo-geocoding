import pandas as pd
import numpy as np
from pathlib import Path, PurePath

# chunk = PurePath("./batch", "./scripts-batch-search", "./file", "./chunked")
full = PurePath("./batch", "./scripts-batch-search", "./file", "./full")

# D:\Bruno\Statistics Canada\Geo\Geocoding\source\odhf_process_6b_deduplicated.xlsx

Path(full).mkdir(parents=True, exist_ok=True)
# Path(chunk).mkdir(parents=True, exist_ok=True)

df = pd.read_csv('./source/IndoorRecFacilities_DIID_r2.csv')

df = df.replace(np.nan, '', regex=True).rename(columns={'ADDRESS': 'STREET'})

df["address"] = df["STC Standard Civic Address"]

df = df.drop(columns=["STC Standard Civic Address"]);

# Set null addresses aside
df_empty = df[df["address"].isnull()]

df_empty.to_csv(full.joinpath("./empty_addresses.csv"), index=False)

# Proceed only with records that have an address
df = df[df["address"].notnull()]

df.to_csv(full.joinpath("./addresses.csv"), index=False)

# max = len(df)
# step = 500000
# i = 0
# start = 0

# while start < max:
#    end = start + step

#    if end > max:
#        end = max

#    df.iloc[start:end].to_csv(chunk.joinpath("./addresses_" + str(i) + ".csv"), index=False)

#    start = end
#    i = i + 1
