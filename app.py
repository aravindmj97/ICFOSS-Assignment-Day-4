import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
# Heart Disease Analysis
 """)
 
st.markdown("Datasource - [Kaggle Dataset](https://www.kaggle.com/ronitf/heart-disease-uci)")

df = pd.read_csv('heart.csv')
st.write('Few rows from of the dataset:', df.head())

st.markdown('**Analysing the relationship between the fields using HeatMap**')
sns.heatmap(df.corr())
st.pyplot()

st.markdown('Relation of **Heart Attack** with **Age**')
st.text("People with heart attack seems to be mostly between ages 40 to 55")
sns.kdeplot(df[df['target']==1]['age'],color="RED")
sns.kdeplot(df[df['target']==0]['age'],color="BLUE")
st.pyplot()

st.markdown('Relation of **Heart Attack** with **Serum Cholestrol**')
st.text("Serum cholestrol doesn't contribute to heart attack")
sns.distplot(df[df['target']==1]['chol'],color="RED")
sns.distplot(df[df['target']==0]['chol'],color="BLUE")
st.pyplot()

st.markdown('Relation of **Heart Attack** with **Chestpain**')
st.text("Chest pain is seen along with heart attack")
sns.distplot(df[df['target']==1]['chol'],color="RED")
sns.distplot(df[df['target']==0]['chol'],color="BLUE")
st.pyplot()