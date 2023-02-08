import requests
import pandas as pd
import streamlit as st
import numpy as np
import csv
import sqlite3
import time
from datetime import datetime


service_key = '4d42486779706d3034365957634870'
data = []

for j in range(1,2):
    url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
    print(url)
    req = requests.get(url)
    content = req.json()
    con = content['tbLnOpendataRentV']['row']

    for h in con:
        dic = {}
        dic['SGG_CD'] = h['SGG_CD']
        dic['SGG_NM'] = h['SGG_NM']
        dic['BJDONG_CD'] = h['BJDONG_CD']
        dic['BJDONG_NM'] = h['BJDONG_NM']
        dic['BOBN'] = h['BOBN']
        dic['BUBN'] = h['BUBN']
        dic['FLR_NO'] = h['FLR_NO']
        dic['CNTRCT_DE'] = h['CNTRCT_DE']
        dic['RENT_GBN'] = h['RENT_GBN']
        dic['RENT_AREA'] = h['RENT_AREA']
        dic['RENT_GTN'] = h['RENT_GTN']
        dic['RENT_FEE'] = h['RENT_FEE']
        dic['BLDG_NM'] = h['BLDG_NM']
        dic['BUILD_YEAR'] = h['BUILD_YEAR']
        dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
        data.append(dic)
# #   ===
# # --
df = pd.DataFrame(data)
df['BOBN'].replace('', np.nan, inplace=True)
df['BUBN'].replace('', np.nan, inplace=True)
df['BLDG_NM'].replace('', np.nan, inplace=True)
df['BUILD_YEAR'].replace('', np.nan, inplace=True)
df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
df = df.dropna()
df['BOBN'] = df['BOBN'].astype('int').astype('str')
df['BUBN'] = df['BUBN'].astype('int').astype('str')
df['FLR_NO'] = df['FLR_NO'].astype('int').astype('str')
df['RENT_AREA'] = df['RENT_AREA'].astype('str') 

print(df)