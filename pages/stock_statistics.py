import streamlit as st
from utilities.localization import LocalizationConfig
from utilities.stcok_analyzer import StockAnalyzer

class StockStatisticsPage:

    def __init__(self):
        pass

    def show_page(self,loc_config:LocalizationConfig):

        
        st.markdown(f"### {loc_config.get_text('config')}")
        st.info(f"{loc_config.get_text('symbol_search')}")

        symbol = st.text_input(loc_config.get_text('symbol'), value="AAPL")
        period = st.selectbox(
            loc_config.get_text("period"),
            options=loc_config.get_subkeys("time_periods"), 
            index=2
        )
        
        prediction_days = st.slider(
            loc_config.get_text("prediction_days"),
            min_value=10,
            max_value=30,
            value=15
        )

        analyzer = StockAnalyzer()

        analyze_btn= st.button(loc_config.get_text("analyze_button"),
                               key="analyze_button")

        if  analyze_btn :
            with st.spinner(loc_config.get_text("loading")):
                if analyzer.fetch_data(symbol, period):
                    #calculate indicators
                    analyzer.calculate_moving_averages()
                    analyzer.calculate_rsi()
                    analyzer.calculate_macd()
                    analyzer.calculate_bollinger_bands()
                    analyzer.calculate_atr()
                    st.session_state["symbol"]=symbol
                    st.session_state["period"]=period
                    st.session_state["prediction_days"]=prediction_days
                    st.session_state["current_price"]=analyzer.data['Close'].iloc[-1]
                    st.session_state["price_change"]=analyzer.data['Close'].pct_change().iloc[-1]
                    st.session_state["volume"]=analyzer.data['Volume'].iloc[-1]
                    st.session_state["rsi"]= analyzer.data['RSI'].iloc[-1]                  
                    st.session_state["analyzer"] = analyzer
        if "analyzer" in st.session_state.keys() :
                analyzer = st.session_state["analyzer"]   
                #display key metrics
                col1, col2, col3, col4 = st.columns(4)
                current_price = analyzer.data['Close'].iloc[-1]
                price_change = analyzer.data['Close'].pct_change().iloc[-1]
                volume = analyzer.data['Volume'].iloc[-1]
                rsi = analyzer.data['RSI'].iloc[-1]
                
                col1.metric(
                    loc_config.get_text("price_stats"),
                    f"{current_price:,.0f} $",
                    f"{price_change:.2%}"
                )
                col2.metric(
                    loc_config.get_text("volume_analysis"),
                    f"{volume:,.0f}"
                )
                col3.metric("RSI", f"{rsi:.2f}")
                col4.metric("ATR", f"{analyzer.data['ATR'].iloc[-1]:.2f}")  
                
                #additional statistics
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"### {loc_config.get_text('price_stats')}")
                    st.write(f"{loc_config.get_text('highest_price')} {analyzer.data['High'].max():,.0f}  $")
                    st.write(f"{loc_config.get_text('lowest_price')} {analyzer.data['Low'].min():,.0f} $")
                    st.write(f"{loc_config.get_text('average_price')} {analyzer.data['Close'].mean():,.0f} $")
                    st.write(f"{loc_config.get_text('price_volatility')} {analyzer.data['Close'].std():,.0f}")
                
                
                with col2:
                    st.markdown(f"### {loc_config.get_text('volume_analysis')}")
                    st.write(f"{loc_config.get_text('average_volume')} {analyzer.data['Volume'].mean():,.0f}")
                    st.write(f"{loc_config.get_text('max_volume')} {analyzer.data['Volume'].max():,.0f}")
                    st.write(f"{loc_config.get_text('min_volume')} {analyzer.data['Volume'].min():,.0f}")
                    volume_trend = loc_config.get_text('increasing') if analyzer.data['Volume'].iloc[-1] > analyzer.data['Volume'].mean() else loc_config.get_text('decreasing')
                    st.write(f"{loc_config.get_text('volume_trend')} {volume_trend}")
                    
                
                with col3:
                    st.markdown(f"### {loc_config.get_text('trend_analysis')}")
                    st.write(f"{loc_config.get_text('current_rsi')} {analyzer.data['RSI'].iloc[-1]:.2f}")
                    macd_signal = loc_config.get_text('bullish') if analyzer.data['MACD'].iloc[-1] > analyzer.data['Signal_Line'].iloc[-1] else loc_config.get_text('bearish')
                    st.write(f"{loc_config.get_text('macd_signal')} {macd_signal}")
                    ma_signal = loc_config.get_text('bullish') if analyzer.data['MA9'].iloc[-1] > analyzer.data['MA13'].iloc[-1] else loc_config.get_text('bearish')
                    st.write(f"{loc_config.get_text('ma_signal')} {ma_signal}")

                #interactive ohlc table 
                st.markdown(f" {loc_config.get_text('price_data') }", unsafe_allow_html=True)                    

                df_display = analyzer.data.copy()
                price_cols = ['Open', 'High', 'Low', 'Close']
                df_display[price_cols] = df_display[price_cols].round(2)
                df_display['Volume'] = df_display['Volume'].astype(int)
                df_display['RSI'] = df_display['RSI'].round(2)
                
                st.dataframe(
                    df_display[['Open', 'High', 'Low', 'Close', 'Volume', 'RSI', 'MACD']].style
                    .background_gradient(subset=['RSI'], cmap='RdYlGn')
                    .background_gradient(subset=['Volume'], cmap='Blues')
                    .format({
                        'Open': '{:,.0f}',
                        'High': '{:,.0f}',
                        'Low': '{:,.0f}',
                        'Close': '{:,.0f}',
                        'Volume': '{:,.0f}',
                        'RSI': '{:.2f}',
                        'MACD': '{:.2f}'
                    }),
                    use_container_width=True,
                    height=200
                )
                    
                #download button for data
                csv = df_display.to_csv().encode('utf-8')
                st.download_button(
                    label= 'download_csv',
                    data=csv,
                    file_name=f'{symbol}_stock_data.csv',
                    mime='text/csv',
                ) 
        st.success(loc_config.get_text("analysis_ready"))
                        
