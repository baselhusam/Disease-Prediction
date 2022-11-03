# Import Libraries
import streamlit as st
import numpy as np
import pickle

# Initial some values
st.session_state.horizontal = True
st.session_state.visibility = 'No'

# Header
st.markdown("<h1 align='center'> Disease Prediction </h1>", unsafe_allow_html=True)
st.markdown("### <br> Please Answer the Following Questions:", unsafe_allow_html=True)
st.markdown("You will have 37 Questions that will determine your desease with 90% accuracy:")
st.markdown("<hr>", unsafe_allow_html=True)

# Questions
l1 = st.radio("Do you have Muscle Pain?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l2 = st.radio("Do you have Itching?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l3 = st.radio("Do you have Altered Sensorium?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l4 = st.radio("Do you have Unsteadiness?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l5 = st.radio("Do you have Yellowing of Eyes?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l6 = st.radio("Do you have Lack of Concentration?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l7 = st.radio("Do you have Chest Pain?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l8 = st.radio("Do you have Diarrhoea?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l9 = st.radio("Do you have Wight Loss?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l10 = st.radio("Do you have Vomiting?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l11 = st.radio("Do you have Fatigue?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l12 = st.radio("Do you have Joint Pain?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l13 = st.radio("Do you have Polyuria?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l14 = st.radio("Do you have Dark Urine?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l15 = st.radio("Do you have Mucoid Sputum?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l16 = st.radio("Do you have Mild Fever?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l17 = st.radio("Do you have Muscle Weakness?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l18 = st.radio("Do you have Coma?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l19 = st.radio("Do you have Family History?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l20 = st.radio("Do you have High Fever?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l21 = st.radio("Do you have Nausea?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l22 = st.radio("Do you have Hip Joint Pain?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l23 = st.radio("Do you have Passage of gases?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l24 = st.radio("Do you have Stomach Pain?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l25 = st.radio("Do you have Blood in Sputum?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l26 = st.radio("Do you have Irritability?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l27 = st.radio("Do you have Pain Behind the Eyes?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l28 = st.radio("Do you have Malaise?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l29 = st.radio("Do you have Fast Hear Rate?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l30 = st.radio("Do you have Rusty Sputum?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l31 = st.radio("Do you have Continuous Feel of Urine?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l32 = st.radio("Do you have Bladder Discomfort?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l33 = st.radio("Do you have Internal Itching?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l34 = st.radio("Do you have Breathlessness?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l35 = st.radio("Do you have Palpitations?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l36 = st.radio("Do you have Stomach Bleeding?",('Yes', 'No'),horizontal=st.session_state.horizontal)
l37= st.radio("Do you have Receiving Unsterile Injections?",('Yes', 'No'),horizontal=st.session_state.horizontal)
st.markdown("<br>", unsafe_allow_html=True)

# The button
col1, col2, col3 = st.columns([1.5,1,1])
flag = False
with col2:
    if st.button("Predict"):
        flag = True
        

# The Prediction
if flag:
    
    st.markdown("<hr>", unsafe_allow_html=True)

    responses = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,
      l19,l20,l21,l22,l23,l24,l25,l26,l27,l28,l29,l30,l31,l32,l33,l34,
       l35,l36,l37]

    lst = []
    for response in responses:
        if response == "Yes":
            lst.append(1)
        elif response == "No":
            lst.append(0)

    X_test = np.array(lst).reshape(1,-1)        
    model = pickle.load(open('model.sav', 'rb'))
    pred = model.predict(X_test)


    st.markdown("<h2 align = 'center'>The Prediction: </h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 align='center' style='color:red'> {pred[0]}  </h3>", unsafe_allow_html=True)






