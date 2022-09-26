from asyncore import read
from cgitb import reset, text
from email.policy import default
from optparse import Values
from re import template
from tkinter.tix import COLUMN
from turtle import title
from unicodedata import name
from wsgiref import headers
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='NF NOTAI')
st.header('Data Analysis 2022')
st.subheader('was the analysis helpful?')



### --- LOAD DATA FRAME
excel_file = 'data.xlsx'
sheet_name = 'data'
sheet_name1 = 'dati'



df=pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A:E', header=6)
df_log=pd.read_excel(excel_file, sheet_name=sheet_name1, usecols='C:E', header=5)




st.dataframe(df)
st.dataframe(df_log)





pie_chart = px.pie(df_log, title='Macroarea', values='Interesse Regionale', names='Macro Area Servizio')

st.plotly_chart(pie_chart)



# --- streamlit selection

department = df['Macro Area Servizio'].unique().tolist()
interest = df['Interesse Regionale'].unique().tolist()

department_selection = st.multiselect('Macro Area Servizio:', department, default=department)

# ---FILTER DATAFRAM BASED ON SELECTION
mask = (df['Macro Area Servizio'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')


df_grouped = df[mask].groupby(by = ['Macro Area Servizio']).sum()[['Interesse Regionale']]
df_grouped = df_grouped.rename(columns={'Macro Area Servizio':'Interesse Regionale'})
df_grouped = df_grouped.reset_index()






bar_chart = px.bar(df_grouped, x = 'Macro Area Servizio', y = 'Interesse Regionale', 
text = 'Interesse Regionale', color_discrete_sequence = ['#F63366']*len(df_grouped), template= 'plotly_white')

st.plotly_chart(bar_chart)
