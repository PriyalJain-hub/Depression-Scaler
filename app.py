import streamlit 
from streamlit_option_menu import option_menu
from predict import show_prediction
from about import show_about
with streamlit.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=["Home", "Depression Scaler"],
        icons=["house","heart"],
        menu_icon="cast",
        default_index=0
    )
if selected=="Home":
    show_about()
if selected =="Depression Scaler":    
    show_prediction()