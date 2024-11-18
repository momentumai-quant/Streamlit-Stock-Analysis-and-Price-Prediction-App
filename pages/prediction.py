import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots 

from utilities.localization import LocalizationConfig

class PredictionPage:

    def __init__(self):
        pass

    def show_page(self,loc_config:LocalizationConfig):
        
        if "analyzer" in st.session_state.keys()   : 
            symbol = st.session_state["symbol"]
            analyzer =  st.session_state["analyzer"]
            prediction_days=st.session_state["prediction_days"]
            st.markdown(f"<div class='subheader-style'>{loc_config.get_text('price_prediction')}</div>", unsafe_allow_html=True)
            feature_columns = analyzer.prepare_features()
            y_test, predictions, rmse = analyzer.train_predict(feature_columns, prediction_days)
            
            col1, col2 = st.columns(2)
            col1.metric(
                loc_config.get_text('prediction_rmse'),
                f"{rmse:,.0f} $"
            )
            col2.metric(
                loc_config.get_text('prediction_accuracy'),
                f"{100 * (1 - rmse/st.session_state['current_price']):.2f}%"
            )
            fig_pred = go.Figure()
            fig_pred.add_trace(
                go.Scatter(
                    x=y_test.index,
                    y=y_test.values,
                    name=loc_config.get_text('actual_price'),
                    line=dict(color='blue')
                )
            )
            fig_pred.add_trace(
                go.Scatter(
                    x=y_test.index,
                    y=predictions,
                    name=loc_config.get_text('predicted_price'),
                    line=dict(color='red', dash='dash')
                )
            )
            fig_pred.update_layout(
                title=loc_config.get_text('price_prediction'),
                height=400,
                template="plotly_white"
            )
            st.plotly_chart(fig_pred, use_container_width=True)