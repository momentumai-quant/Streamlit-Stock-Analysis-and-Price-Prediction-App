import streamlit as st
import numpy as np
import pandas as pd
from utilities.localization import LocalizationConfig
from utilities.visualization import *
class AnalysisPage:

    def __init__(self):
        pass

    def show_page(self,loc_config:LocalizationConfig): 

        if "analyzer" in st.session_state.keys()   : 
            symbol = st.session_state["symbol"]
            analyzer =  st.session_state["analyzer"]
            #st.write(loc_config.get_text("technical_indicators"))

            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"<div class='subheader-style'>{loc_config.get_text('price_movement')}</div>", unsafe_allow_html=True)
                price_fig = create_price_chart(analyzer.data, symbol)
                st.plotly_chart(price_fig, use_container_width=True)
            
            with col2:
                st.markdown(f"<div class='subheader-style'>{loc_config.get_text('technical_indicators')}</div>", unsafe_allow_html=True)
                indicators_fig = create_technical_indicators_chart(analyzer.data)
                st.plotly_chart(indicators_fig, use_container_width=True)