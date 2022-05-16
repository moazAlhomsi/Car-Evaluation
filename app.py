# Core pkgs
import streamlit as st
from EDA import run_EDA_app
from ML import run_ML_app



def main() :
	st.set_page_config(page_title='Car-Evaluation',
				   	   page_icon='🏎️')



	menu = ["Home","EDA","ML"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.header("Welcome to Car-Eval Model")

		st.markdown("""
			The model evaluates cars according to the following concept structure:

CAR car acceptability

. PRICE overall price

. . buying buying price

. . maint price of the maintenance


. TECH technical characteristics

. . COMFORT comfort

. . . doors number of doors

. . . persons capacity in terms of persons to carry

. . . lug_boot the size of luggage boot

. . safety estimated safety of the car

Car Evaluation Database was derived from a simple hierarchical decision model originally developed for the demonstration of DEX, M. Bohanec, V. Rajkovic: Expert system for decision making. Sistemica 1(1), pp. 145-157, 1990.)
			""")
		st.markdown("https://archive.ics.uci.edu/ml/datasets/Car+Evaluation")

	elif choice == "EDA":
		run_EDA_app()

	elif choice == "ML":
		run_ML_app() 
    

if __name__ == '__main__':
	main()
