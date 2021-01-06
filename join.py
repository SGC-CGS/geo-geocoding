import pandas as pd
import requests as req
import numpy as np

vanc = pd.read_excel('BC - Vancouver - Indoor.xlsx').set_index('Full address')
qc_mtl = pd.read_excel('QC_MTL_Merged - Indoor.xlsx').set_index('Full Address')
sask = pd.read_excel('SASK_MAN - Regina (SK) - Indoor.xlsx').set_index('Full address')
winn = pd.read_excel('SASK_MAN - Winnipeg (MN) - Indoor.xlsx').set_index('Full address')

geocoded = pd.read_excel('geocoded.xlsx', index_col=0)

vanc = vanc.join(geocoded).reset_index().rename(columns={'index': 'address'})
qc_mtl = qc_mtl.join(geocoded).reset_index().rename(columns={'index': 'address'})
sask = sask.join(geocoded).reset_index().rename(columns={'index': 'address'})
winn = winn.join(geocoded).reset_index().rename(columns={'index': 'address'})

vanc.to_excel("./geocoded/vancouver.xlsx", index=False)
qc_mtl.to_excel("./geocoded/montreal.xlsx", index=False)
sask.to_excel("./geocoded/regina.xlsx", index=False)
winn.to_excel("./geocoded/winnipeg.xlsx", index=False)

