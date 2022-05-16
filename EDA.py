import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
@st.cache
def laod_data(data):
	df = pd.read_csv(data)
	return data 

def run_EDA_app():
	st.subheader("EDA Analysis")
	df = pd.read_csv('car_eval_edited.csv')
	df_cleaned = pd.read_csv('data_tranformed.csv')

	submenu = st.sidebar.selectbox('submenu',['Descriptive','Plots'])

	if submenu == 'Descriptive':
		st.markdown('Dataframe')
		st.dataframe(df)
		with st.expander("Data Values"):

			col1,col2 = st.columns([1,1])
			with col1:
				for i in df[['buying','maint','doors']]:
					st.table(df[i].value_counts())

			with col2:
				for i in df[['persons','lug_boot','safety']]:
					st.table(df[i].value_counts())		


	if submenu == 'Plots':
		
		
		fig = plt.figure()
		sns.countplot(df['class'])
		st.pyplot(fig)

		st.dataframe(df['class'].value_counts())


				