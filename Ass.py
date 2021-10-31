from altair.vegalite.v4.schema.channels import Column
from google.protobuf import message
from sqlalchemy.orm.session import Session
import streamlit as st
from streamlit.proto.Image_pb2 import Image
from matplotlib import pyplot as plt
import  plotly as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor



df=pd.read_csv('Placement_Data_Full_Class.csv')




st.title("Prediction for campus recruitment")
st.markdown('---')
col1,col2=st.beta_columns(2)
col1.image("simg.gif")
st.write("""Hello....

This is my assignment project prediction and this is based on campus placement recruitment.
It predict a data in form of placed or unplaced students.
""")
col3,col4=st.beta_columns(2)
col3.header("     ")
col4.header("-Made by Shruti Shukla")
numerical_df=df.select_dtypes(["float64","int64"])

st.dataframe(df)

st.image("pl.gif",width=300)

