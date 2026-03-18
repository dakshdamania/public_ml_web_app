import streamlit as st
import numpy as np
import pickle

# Load trained model
loaded_model = pickle.load(open('parkinsons_model.sav', 'rb'))

st.title("Parkinson's Disease Prediction Web App")

st.write("Enter the following voice measurement values to predict Parkinson's Disease.")

# Input fields
fo = st.number_input("MDVP:Fo(Hz)")
fhi = st.number_input("MDVP:Fhi(Hz)")
flo = st.number_input("MDVP:Flo(Hz)")
jitter_percent = st.number_input("MDVP:Jitter(%)")
jitter_abs = st.number_input("MDVP:Jitter(Abs)")
rap = st.number_input("MDVP:RAP")
ppq = st.number_input("MDVP:PPQ")
ddp = st.number_input("Jitter:DDP")

shimmer = st.number_input("MDVP:Shimmer")
shimmer_db = st.number_input("MDVP:Shimmer(dB)")
apq3 = st.number_input("Shimmer:APQ3")
apq5 = st.number_input("Shimmer:APQ5")
apq = st.number_input("MDVP:APQ")
dda = st.number_input("Shimmer:DDA")

nhr = st.number_input("NHR")
hnr = st.number_input("HNR")

rpde = st.number_input("RPDE")
dfa = st.number_input("DFA")
spread1 = st.number_input("Spread1")
spread2 = st.number_input("Spread2")
d2 = st.number_input("D2")
ppe = st.number_input("PPE")

# prediction button
if st.button("Predict"):

    input_data = np.array([
        fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,
        shimmer,shimmer_db,apq3,apq5,apq,dda,
        nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe
    ]).reshape(1,-1)

    prediction = loaded_model.predict(input_data)

    if prediction[0] == 0:
        st.success("The person is Healthy")
    else:
        st.error("Parkinson's Disease Detected")