
import tensorflow as tf 
import streamlit as st 

st.write(tf.__version__)

from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd 

st.write(pd.__version__)
st.write("Done?")
