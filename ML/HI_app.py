import streamlit as st
import pickle
model = pickle.load(open("HI_model.pkl","rb"))

age = st.text_input("Age")
gender = st.text_input("Gender")
bmi = st.text_input("BMI")
children = st.text_input("children")
smoke = st.text_input("Do you smoke ")
smoke_enc = 1 if smoke == "yes" else 0
gender_enc = 1 if gender == "female" else 0
if st.button("Submit"):
    age = int(age)
    bmi = float(bmi)
    children = int(children)
    q = [[age,gender_enc,smoke_enc,bmi,children]]
    yp = round(model.predict(q)[0],2)
    st.write("Your Premium : " + str(yp))
    

