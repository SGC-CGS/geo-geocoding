import pandas as pd
import requests as req
import numpy as np

# vanc = pd.read_excel('BC - Vancouver - Indoor.xlsx', index_col=0)
# qc_mtl = pd.read_excel('QC_MTL_Merged - Indoor.xlsx', index_col=0)
# sask = pd.read_excel('SASK_MAN - Regina (SK) - Indoor.xlsx', index_col=0)
# winn = pd.read_excel('SASK_MAN - Winnipeg (MN) - Indoor.xlsx', index_col=0)
odhf = pd.read_excel('odhf_process_6b_deduplicated.xlsx', index_col=0)

# vanc = vanc[['Full address']]
# qc_mtl = qc_mtl[['Full Address']]
# sask = sask[['Full address']]
# winn = winn[['Full address']]
odhf = odhf[['address']]

# vanc.columns = ["clean_addr"]
# qc_mtl.columns = ["clean_addr"]
# sask.columns = ["clean_addr"]
# winn.columns = ["clean_addr"]

total = pd.concat([winn])

df = total.drop_duplicates(subset='clean_addr').dropna()

df.to_excel("unique_addr.xlsx", index=False)