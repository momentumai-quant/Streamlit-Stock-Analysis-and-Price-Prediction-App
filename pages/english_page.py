"""
Main Streamlit app
===========================

Home Page for Stock Analysis Dashbaord to hanle all other pages and navigations

Author: https://github.com/momentumai-quant
Last Modified: 2024-11-11
"""

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
import streamlit as st

#machine learning
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
 
#setup
from pages.stock_statistics import StockStatisticsPage
from pages.prediction import PredictionPage
from pages.analysis import AnalysisPage

from utilities.localization import LocalizationConfig
from streamlit_option_menu import option_menu
#===========================
#configs
#===========================
loc_config = LocalizationConfig(lang='en')

st.set_page_config(
    page_title=loc_config.get_text("dashboard_title"),
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        visibility: hidden;
    }
    [data-testid="stSidebarCollapsedControl"]{
        visibility: hidden;
    }
    </style>
    """, 
    unsafe_allow_html=True
) 

 

 
                
#language switch
lang_btn= st.button( "🌐 " +  loc_config.get_text('language_selector'),  key='lang_switch', )         
if lang_btn:
    st.switch_page("pages/persian_page.py")    


selected_page = option_menu(
    menu_title=None,  
    options=[loc_config.get_text("nav_stock_statistics"),
             loc_config.get_text("nav_analysis"), 
             loc_config.get_text("nav_prediction")],
    icons=["house", "file-earmark-text", "file-earmark-text"],  
    menu_icon="cast", 
    default_index=0,  
    orientation="horizontal",   
)

if selected_page == loc_config.get_text("nav_stock_statistics"):
    StockStatisticsPage().show_page(loc_config=loc_config) 

elif selected_page == loc_config.get_text("nav_analysis"):
    AnalysisPage().show_page(loc_config=loc_config)

elif selected_page == loc_config.get_text("nav_prediction"):
    PredictionPage().show_page(loc_config=loc_config)



