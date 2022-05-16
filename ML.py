import streamlit as st
import joblib
import os
import numpy as np


attribute_info = """
	Attributes Info
- buying ['vhigh':3,'high': 0, 'med': 2, 'low': 1]
- maint ['vhigh': 3,'high': 0, 'med': 2, 'low': 1]
- doors ['2': 0, '3': 1, '4': 2, '5more': 3]
- persons ['2': 0, '4': 1, 'more': 2]
- lug_boot ['small': 1, 'med': 2, 'big': 0]
- safety ['low': 1, 'med': 2, 'high': 0]
- class ['unacc': 1, 'acc': 0]
"""


label_buy_main = {'vhigh':3,'high': 0, 'med': 2, 'low': 1}
label_door = {'2': 0, '3': 1, '4': 2, '5more': 3}
label_persons = {'2': 0, '4': 1, 'more': 2}
label_lug = {'small': 1, 'med': 2, 'big': 0}
label_safety = {'low': 1, 'med': 2, 'high': 0}
label_class = {'unacc': 1, 'acc': 0}

# def get_fvalue(val):
# 	feature_dict = {'vhigh':3,'high': 0, 'med': 2, 'low': 1}
# 	for key,value in feature_dict.items():
# 		if val == key:
# 			return value

def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value

#Load ML model
@st.cache(allow_output_mutation=True)
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def run_ML_app():
	st.header('ML Model')
	with st.expander('Info'):
		st.subheader(attribute_info)
	loaded_model = load_model('model/rf.pkl')
					 
	col1,col2 = st.columns(2)
	with col1:
		buying = st.radio("Buying price",['high','low','med','vhigh'])
		maint = st.radio("Maintainance cost",['high','low','med','vhigh'])
		doors = st.radio("Doors",['2','3','4','5more'])

	with col2:
		persons = st.radio("Persons capacity",['2','4','more'])
		lug_boot = st.radio("Size of luggage boot",['big','small','med'])
		safety = st.radio("Safety of the car",['high','low','med'])

	with st.expander("Selected Options:"):
		result = {"Buying price":buying,
				  "Maintainance cost":maint,
				  "Doors":doors,
				  "Persons capacity":persons,
				  "Size of luggage boot":lug_boot,
				  "Safety of the car":safety}
		st.write(result)
		encoded_result = []
		for i in result.values():
			
			if i in ['high','low','med','vhigh']:
				res = get_value(i,label_buy_main)
				encoded_result.append(res)

			elif i in ['2','3','4','5more']:
				res = get_value(i,label_door)
				encoded_result.append(res)

			elif i in ['2','4','more']:
				res = get_value(i,label_persons)
				encoded_result.append(res)

			elif i in ['big','small','med']:
				res = get_value(i,label_lug)
				encoded_result.append(res)

			elif i in ['high','low','med']:
				res = get_value(i,label_safety)
				encoded_result.append(res)			



# st.write(encoded_result)
	with st.expander("Prediction Results"):
		single_sample = np.array(encoded_result).reshape(1,-1)

		
		prediction = loaded_model.predict(single_sample)
		pred_prob = loaded_model.predict_proba(single_sample)
		st.write(prediction)
		if prediction == 1:
			st.error("An outcome of {} shows the evaluation of car is Unaccepted ".format(prediction[0]))

		else:
			st.success("An outcome of {} shows the evaluation of car is Accepted".format(prediction[0]))


