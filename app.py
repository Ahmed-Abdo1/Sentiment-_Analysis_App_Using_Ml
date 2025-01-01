import streamlit as st
import Helper
import sklearn
import pickle


model=pickle.load(open("Models/model (1).pkl",'rb'))
vectorize=pickle.load(open("Models/vectorize.pkl",'rb'))

st.title("Sentiment Analysis Using Ml")


state=st.button('Predict')
text=st.text_input('Please Enter your review')
token = Helper.prepreoccessing(text)
vectorize_data=vectorize.transform([token])
prediction=model.predict(vectorize_data)


if state :
    st.text(prediction)
