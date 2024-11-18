import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots 

def create_price_chart(data, 
                       symbol,
                       ohlc_name="Price",
                       ma_9_name="Moving Average 9 ",
                       ma_13_name="Moving Average 13 ",
                       data_name="Date",
                       plot_name="Price And Moving Average Chart For Symbol "): 
    fig = go.Figure()
    
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name=ohlc_name
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['MA9'],
            name=ma_9_name,
            line=dict(color='blue', width=1)
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['MA13'],
            name=ma_13_name,
            line=dict(color='orange', width=1)
        )
    )
    
    fig.update_layout(
        title=f" {symbol} {plot_name}",
        yaxis_title=ohlc_name,
        xaxis_title=data_name,
        height=500,
        template="plotly_white",
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        )
    )
    
    return fig

def create_technical_indicators_chart(data,
                                      rsi_name="RSI Indicator",
                                      macd_name="MACD Indicator",
                                      atr_name="ATR Indicator",
                                      signal_name="Signal Line",
                                      macd_hist_name="MACD Histogram"): 
    fig = make_subplots(
        rows=3,
        cols=1,
        subplot_titles=(rsi_name,
                        macd_name,
                        atr_name ),
        vertical_spacing=0.1,
        row_heights=[0.33, 0.33, 0.33]
    )
    
    
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['RSI'],
            name="RSI",
            line=dict(color='purple')
        ),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['MACD'],
            name="MACD",
            line=dict(color='blue')
        ),
        row=2, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['Signal_Line'],
            name=signal_name,
            line=dict(color='orange')
        ),
        row=2, col=1
    )
    
    fig.add_trace(
        go.Bar(
            x=data.index,
            y=data['MACD_Histogram'],
            name=macd_hist_name
        ),
        row=2, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['ATR'],
            name="ATR",
            line=dict(color='red')
        ),
        row=3, col=1
    )
    
    fig.update_layout(
        height=800,
        showlegend=True,
        template="plotly_white"
    )
    
    return fig
