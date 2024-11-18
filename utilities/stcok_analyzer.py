
import numpy as np
import pandas as pd
import streamlit as st

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import yfinance as yf

class StockAnalyzer:
    def __init__(self):
        self.data = None
        self.symbol = None
    
    def fetch_data(self, symbol, period='1y'): 
        try:
            stock = yf.Ticker(symbol)
            self.data = stock.history(period=period)
            self.symbol = symbol
            return True
        except Exception as e:
            st.error(f"error fetching data: {e}")
            return False
    
    def calculate_moving_averages(self): 
        self.data['MA9'] = self.data['Close'].rolling(window=9).mean()
        self.data['MA13'] = self.data['Close'].rolling(window=13).mean()
        self.data['MA20'] = self.data['Close'].rolling(window=20).mean()
        self.data['MA30'] = self.data['Close'].rolling(window=30).mean()
    
    def calculate_rsi(self, periods=14): 
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
    
    def calculate_macd(self): 
        exp1 = self.data['Close'].ewm(span=12, adjust=False).mean()
        exp2 = self.data['Close'].ewm(span=26, adjust=False).mean()
        self.data['MACD'] = exp1 - exp2
        self.data['Signal_Line'] = self.data['MACD'].ewm(span=9, adjust=False).mean()
        self.data['MACD_Histogram'] = self.data['MACD'] - self.data['Signal_Line']
    
    def calculate_bollinger_bands(self): 
        self.data['BB_Middle'] = self.data['Close'].rolling(window=20).mean()
        bb_std = self.data['Close'].rolling(window=20).std()
        self.data['BB_Upper'] = self.data['BB_Middle'] + (bb_std * 2)
        self.data['BB_Lower'] = self.data['BB_Middle'] - (bb_std * 2)
    
    def calculate_atr(self, period=14): 
        high_low = self.data['High'] - self.data['Low']
        high_close = np.abs(self.data['High'] - self.data['Close'].shift())
        low_close = np.abs(self.data['Low'] - self.data['Close'].shift())
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = np.max(ranges, axis=1)
        self.data['ATR'] = true_range.rolling(window=period).mean()
    
    def prepare_features(self): 
        self.data['Returns'] = self.data['Close'].pct_change()
        self.data['Last_day_Close'] = self.data['Close'].shift(1)
        self.data['Last_day_Open'] = self.data['Open'].shift(1)
        self.data['Volatility'] = self.data['Returns'].rolling(window=20).std()
        
        feature_columns = [
            "Last_day_Close",
            "Last_day_Open",
            'RSI',
            'MACD',
            'ATR',
            'Returns',
            'Volatility',
            'MA9',
            'MA13',
            'MA20', 
            'MA30'
        ]
        
        self.data = self.data.dropna()
        return feature_columns
    
    def train_predict(self, feature_columns, prediction_days=30): 
        X = self.data[feature_columns]
        y = self.data['Close']
        
        train_size = len(self.data) - prediction_days
        X_train = X[:train_size]
        y_train = y[:train_size]
        X_test = X[train_size:]
        y_test = y[train_size:]
        
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            min_samples_split=5,
            random_state=42,
            n_jobs=-1
        )
        model.fit(X_train_scaled, y_train)
        
        predictions = model.predict(X_test_scaled)
        mse = np.mean((predictions - y_test) ** 2)
        rmse = np.sqrt(mse)
        
        return y_test, predictions, rmse
