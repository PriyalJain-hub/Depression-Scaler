import numpy as np
import streamlit as st 
import pandas as pd

def show_about():
    st.title("About Depression Scaler")
    st.write('<p style="font-size:18px">This project is based on the <b style="color:#83D475">Depression Anxiety Stress Scales Responses</b> dataset from <b style="color:#20beff">Kaggle</b>. <p style="font-size:18px">Early diagnosis and professional aid can help the victims of depression overcome it. This machine learning project aims to build a model that scales depression based on series of questions asked to the user and through survey analysis, predict the scale of depression the user is experiencing. This would help the user understand their mental state and also make them aware if professional help is necessary. This project aims to build a model that can be used by any user in the easiest way at their own convenience.</p></p>',unsafe_allow_html=True)
    
    st.write('<p style="font-size:20px">Interpretation Guide:</p>',unsafe_allow_html=True)
    st.write('<p style="font-size:18px">The ml model is trained based on DASS- 42 system and Ten Item Personality Inventory questions.</p>',unsafe_allow_html=True)
    st.write('<p style="font-size:18px">The severity labels are used to describe the full range of scores in the population, so ‘mild’ for example means that the person is above the population mean but probably still below the typical severity of someone seeking help (i.e. it does not mean a mild level of disorder). </p>',unsafe_allow_html=True)