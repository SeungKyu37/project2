import lxml
import requests
from bs4 import BeautifulSoup
import pandas as pd

service_key = '564b7852646a686a34336f4f6c5571'
url = f'http://openapi.seoul.go.kr:8088/{service_key}/xml/tbLnOpendataRtmsV/1/5/2022'

result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, "lxml") # html.parser 

years            = soup.find_all('acc_year')         # 접수년월
sgg_cds          = soup.find_all('sgg_cd')           # 자치구코드
sgg_nms          = soup.find_all('sgg_nm')           # 자치구명
bjdong_cds       = soup.find_all('bjdong_cd')        # 법정동코드
bjdong_nms       = soup.find_all('bjdong_nm')        # 법정동명
land_gbns        = soup.find_all('land_gbn')         # 지번구분
land_gbn_nms     = soup.find_all('land_gbn_nm')      # 지번구분명
land_gbn_nms     = soup.find_all('land_gbn_nm')      # 지번구분명
bonbeons         = soup.find_all('bonbeon')          # 본번
bubeons          = soup.find_all('bubeon')           # 부번
bldg_nms         = soup.find_all('bldg_nm')          # 건물명
deal_ymds        = soup.find_all('deal_ymd')         # 계약일
obj_amts         = soup.find_all('obj_amt')          # 물건금액(만원)
bldg_areas       = soup.find_all('bldg_area')        # 건물면적(㎡)
tot_areas        = soup.find_all('tot_area')         # 토지면적(㎡)
floors           = soup.find_all('floor')            # 층
right_gbns       = soup.find_all('right_gbn')        # 권리구분
cntl_ymds        = soup.find_all('cntl_ymd')         # 취소일
build_years      = soup.find_all('build_years')      # 건축년도
house_types      = soup.find_all('house_type')       # 건물용도
req_gbn          = soup.find_all('req_gbn')          # 신고구분
rdealer_lawdnms  = soup.find_all('rdealer_lawdnm')   # 신고한 개업공인중개사 시군구명

%%time

sgg_cd_list         = []
sgg_nm_list         = []
bjdong_cd_list      = []
bjdong_nm_list      = []
bobn_list           = []
bubn_list           = []
flr_no_list         = []
cntrct_de_list      = []
rent_gbn_list       = []
rent_area_list      = []
rent_gtn_list       = []
rent_fee_list       = []
bldg_nm_list        = []
build_year_list     = []
house_gbn_nm_list   = []

for year, sgg_cd, bldg_nm, obj_amt, house_type, rdealer_lawdnm in zip(years, sgg_cds, bldg_nms, obj_amts, house_types, rdealer_lawdnms):
    year_list.append(year.get_text())
    sgg_cd_list.append(sgg_cd.get_text())
    bldg_nm_list.append(bldg_nm.get_text())
    obj_amt_list.append(obj_amt.get_text())
    house_type_list.append(house_type.get_text())
    rdealer_lawdnm_list.append(rdealer_lawdnm.get_text())

df = pd.DataFrame({ 
    "sgg_cd": sgg_cd_list, 
    "bldg_nm" : bldg_nm_list,
    "obj_amt": obj_amt_list,
    "house_type" : house_type_list,
    "rdealer_lawdnm": rdealer_lawdnm_list
})

df