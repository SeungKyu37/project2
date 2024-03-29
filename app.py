# 홈

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import math
import sqlite3
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta
import openai
st.title(':house_buildings:내 방, 어디:eyes:?')

from search import run_search
from predict import run_predict
from suggestions import run_suggestions
from update import update_data
from mean_db import dong_j_d_mean
from chatbot import chatrun


selected3 = option_menu(None, ["🏠Home", "🔎전월세 검색",  "📊전세 예측", '💬챗봇', '👂건의사항'], 
    icons = ['🏠', '🔎', '📊', '💬','👂️'],
    default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)

# 홈 탭
if selected3 == "🏠Home":
    data = update_data()
    data2 = data.copy()

    # 실거래 현황
    st.markdown("""
    ## :crown:실거래 현황
    - *현재까지의 서울시 집에 대한 실거래가 현황입니다!*

    """)
    st.subheader('실거래 현황 (최신순)')
    # st.write("기간 : " + f'{before_month}' + " ~ " +f'{before_day}' + " (계약일 기준)")
    st.write("매일 오후 10시 데이터 갱신")
    latest = data.loc[1,['CNTRCT_DE']].values[0]
    st.write("기간 : 2022-01-01 ~ " +f'{latest}' + " (계약일 기준)")
    # data = data[data['CNTRCT_DE']>=f'{before_month}']

    data['FLR_NO'] = data['FLR_NO'].astype(str) + '층'
    cols = ['BOBN', 'BUBN']
    data['번지'] = data[cols].apply(lambda row: '-'.join(row.values.astype(str))
                                            if row['BUBN'] != 0
                                            else row['BOBN'], axis=1)
    data['BLDG_NM'] = data['BLDG_NM'].str.replace('아파트', '')
    data['BLDG_NM'] = data['BLDG_NM'].str.replace('오피스텔', '')                             
    cols1 = ['SGG_NM', 'BJDONG_NM', '번지', 'BLDG_NM', 'HOUSE_GBN_NM', 'FLR_NO']
    data['주소'] = data[cols1].apply(lambda row:' '.join(row.values.astype(str)),axis=1)
    data = data.drop(['SGG_CD', 'BJDONG_CD', 'SGG_NM', 'BJDONG_NM', 'BOBN', 'BUBN', 'FLR_NO', 'BLDG_NM', '번지', 'HOUSE_GBN_NM'], axis=1)
    data['RENT_AREA'] = data['RENT_AREA'].apply(lambda x: math.trunc(x / 3.3058))
    data.columns = ['계약일', '전월세 구분', '임대면적(평)', '보증금(만원)', '임대료(만원)', '건축년도', '주소']
    data = data[['계약일', '주소', '보증금(만원)', '임대료(만원)', '임대면적(평)', '건축년도', '전월세 구분']]
    data = data.reset_index(drop=True)
    data.index = data.index+1
    st.write(data)


# 전월세 검색 탭
elif selected3 == "🔎전월세 검색":
    run_search()

# 전세 시세 예측 탭 
elif selected3 == "📊전세 예측":
    data = update_data()
    run_predict(data)

elif selected3 == "💬챗봇":
    chatrun()
    

# 건의사항 탭
elif selected3 == "👂건의사항":
    run_suggestions()
else:
    selected3 == "🏠Home"
