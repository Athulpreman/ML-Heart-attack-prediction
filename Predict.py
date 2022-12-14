import streamlit as st
import pandas as pd
import pickle
import sklearn
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

st.write("""
# Heart Attack Prediction
 """)
BloodPressure=Cholestrol=BloodSugar=MaximumHeartRate="ap"
svm_classifier = open('Attack_Model.pkl','rb')
classifier = pickle.load(svm_classifier)
b1=b2=b3=0
#NoMajorVessels=0
age = st.text_input("Enter the Age  ")
#gender =  st.text_input("Enter the Gender (M/F)  ")
gender=st.radio("Select gender",('Male','Female'))
if gender=='Male':
	gender=1
else:
	gender=0
ChestPainType = st.radio("Enter the Chest pain Type ",("No Chest pain","Angina","Aortic dissection","Pericarditis"))
if ChestPainType=="Angina":
	ChestPainType=1
elif ChestPainType=="Aortic dissection":
	ChestPainType=2
elif ChestPainType=="Pericarditis":
	ChestPainType=3
else:
	ChestPainType=0
BloodPressure = st.text_input("Enter Resting Blood Pressure  ")
Cholestrol = st.text_input("Enter Cholestrol level  ")
BS = st.radio("Select Fasting Blood Sugar",('Greater than or equel to 120 mg','Less than 120 mg'))
if BS=="Greater than or equel to 120 mg":
	BloodSugar=1
else:
	BloodSugar=0
abnormality = st.radio("Is there any abnormality in ECG",('Yes','No'))
if abnormality=='Yes':
	ECG=1
else:
	ECG=0
MaximumHeartRate = st.text_input("Enter maximum heart rate achieve ")
Exerc = st.radio("Do you exercise regularly",('Yes','No'))
if Exerc=='Yes':
	Exercise=0
else:
	Exercise=1
MajorVessels = st.radio("Is any major vessels(to heart) damaged ",("No","Yes"))
if MajorVessels=="Yes":
	#a1=st.checkbox("Aorta")
	#a2=st.checkbox("Vena Cava")
	#a3=st.checkbox("Pulmonary vein or artery")
	if st.checkbox("Aorta"):
		b1=1
	else:
		b1=0
	if st.checkbox("Vena Cava"):
		b2=1
	else:
		b2=0
	if st.checkbox("Pulmonary vein or artery"):
		b3=1
	else:
		b3=0
else:
	NoMajorVessels=0

submit = st.button("Predict")
if submit:
	if BloodPressure=="" or Cholestrol=="" or BloodSugar=="" or MaximumHeartRate=="":
		st.warning("Enter every details correctly..")
	else:
		NoMajorVessels = b1 + b2 + b3
		result = classifier.predict([[age, gender, ChestPainType, BloodPressure, Cholestrol, BloodSugar, ECG,
									  MaximumHeartRate, Exercise, NoMajorVessels]])
		if result == 0:
			st.markdown("I am very sorry... ***It seems you will have heart attack*** :cry:")
			st.warning(
				"Take required precautions as soon as possible. Visit the following site for more details.    https://www.medicinenet.com/heart_attack_and_atherosclerosis_prevention/article.htm")

		else:
			st.markdown("Congrats..!! ***You wont have heart attack.*** :smile:")
			st.warning("Exercise regularly for better health.")
