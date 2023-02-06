import requests
import pandas as pd
import streamlit as st
import numpy as np
import csv
import sqlite3

# #[1]DB생성-->Conncetion객체의-->connect()함수를 사용하여 생성
# dbConn=sqlite3.connect('mydata.db')
# print(type(dbConn)) #sqlite3.Conncetion 객체.

# #[2]DB커서 객체 생성-->Conncetion객체인 dbConn을 사용해 Cursor객체를 생성.
# cs=dbConn.cursor()
# print(type(cs)) #sqlite3.Cursor객체.

# #[3]DB테이블 생성
# # cs.execute("Create table if not exists tbl_PublicAPI)_")
# cs.execute('Create table if not exists tbl_PublicAPI(SGG_CD varchar, SGG_NM varchar, BJDONG_CD varchar, BJDONG_NM varchar, BOBN varchar, BUBN varchar, FLR_NO varchar, CNTRCT_DE varchar, RENT_GBN varchar, RENT_AREA varchar, RENT_GTN varchar, RENT_FEE varchar, BLDG_NM varchar, BUILD_YEAR varchar, HOUSE_GBN_NM varchar)')

# #[1]csv파일 읽기-->open()사용-->csv.reader()메서드 사용하여 한 줄씩 읽기.
# fileName="data/bds_data.csv"
# file=open(fileName,"r")
# reader=csv.reader(file)



# #[3]순회하면서 할 일 처리.
# arr=[]

# for row in reader:
#     # print(row)
#     arr.append(row)
    
# for row in arr:
#     strSQL="INSERT INTO tbl_PublicAPI(SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,FLR_NO,CNTRCT_DE,RENT_GBN,RENT_AREA,RENT_GTN,RENT_FEE,BLDG_NM,BUILD_YEAR,HOUSE_GBN_NM)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
#     cs.execute(strSQL,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))

# dbConn.commit()

#[2]DB연결 및 커서 객체 생성
dbConn=sqlite3.connect("mydata.db")
cs=dbConn.cursor()

#[4]DB데이터 출력
def db_list():
    cs.execute('SELECT * FROM tbl_PublicAPI')
    sugg = cs.fetchall()
    return sugg

list = db_list()     
df = pd.DataFrame(list, columns=['SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','BOBN','BUBN','FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR','HOUSE_GBN_NM'])     
df = df.drop(0, axis=0)
st.dataframe(df)

cs.close()
dbConn.close()

# service_key = '4d42486779706d3034365957634870'
# data = []

# for j in range(1,2):
#     url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/{1+((j-1)*1000)}/{j*1000}'
#     print(url)
#     req = requests.get(url)
#     content = req.json()
#     con = content['tbLnOpendataRentV']['row']

#     for h in con:
#         dic = {}
#         dic['SGG_CD'] = h['SGG_CD']
#         dic['SGG_NM'] = h['SGG_NM']
#         dic['BJDONG_CD'] = h['BJDONG_CD']
#         dic['BJDONG_NM'] = h['BJDONG_NM']
#         dic['BOBN'] = h['BOBN']
#         dic['BUBN'] = h['BUBN']
#         dic['FLR_NO'] = h['FLR_NO']
#         dic['CNTRCT_DE'] = h['CNTRCT_DE']
#         dic['RENT_GBN'] = h['RENT_GBN']
#         dic['RENT_AREA'] = h['RENT_AREA']
#         dic['RENT_GTN'] = h['RENT_GTN']
#         dic['RENT_FEE'] = h['RENT_FEE']
#         dic['BLDG_NM'] = h['BLDG_NM']
#         dic['BUILD_YEAR'] = h['BUILD_YEAR']
#         dic['HOUSE_GBN_NM'] = h['HOUSE_GBN_NM']
#         data.append(dic)
# #   ===
# # --
# df = pd.DataFrame(data)
# df['BOBN'].replace('', np.nan, inplace=True)
# df['BUBN'].replace('', np.nan, inplace=True)
# df['BLDG_NM'].replace('', np.nan, inplace=True)
# df['BUILD_YEAR'].replace('', np.nan, inplace=True)
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'] = df['CNTRCT_DE'].apply(lambda x: pd.to_datetime(str(x), format="%Y/%m/%d"))
# df['CNTRCT_DE'] = df['CNTRCT_DE'].astype('str')
# df['CNTRCT_DE'].replace('T00:00:00', '', inplace=True)
# df = df.dropna()
# st.write(df)
# # df.to_csv('data.csv',encoding='euc-kr', index=False)

