import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import seaborn as sns
import os
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings("ignore")
import matplotlib.font_manager as fonm
# import prophet
# import yfinance as yf
# from prophet import Prophet
import matplotlib.dates as mdates
from matplotlib import cm
from tensorflow import keras
from keras.models import Model
from keras.layers import Dense, LSTM
from tensorflow.python.keras import Sequential
import plotly.express as px
import plotly.graph_objects as go

from mean_db import ml_data
from lstm_model import dl_model

def prediction2(data):
    st.header('전세 실거래가 예측')

    SGG_NM_list = data['SGG_NM'].unique()
    date = data['CNTRCT_DE'].max()
    print(SGG_NM_list)

    SELECTED_SGG = st.selectbox('원하는 구를 선택하세요',(SGG_NM_list))

    check2 = st.checkbox(f'{SELECTED_SGG} '"실거래가 예측 수치로 보기")
    results, df_future = dl_model(data, SELECTED_SGG)

    if check2:
        st.subheader(f'{SELECTED_SGG} ''실거래가 예측 수치')
        st.dataframe(df_future[['Date','Forecast']].set_index('Date'))
        st.write("👉 Date: 날짜 ,"'Forecast: 예측가')
    else:
        st.subheader(f'{SELECTED_SGG} ''실거래가 예측 그래프') 
        fig, ax = plt.subplots()
        ax.plot(results['RENT_GTN'], label='past')
        ax.plot(results['Forecast'],label='prediction')
        ax.legend()
        plt.title('LSTM Graph')
        st.pyplot(fig)
   
