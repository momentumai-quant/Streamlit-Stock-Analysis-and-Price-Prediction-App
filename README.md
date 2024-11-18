## Stock Analysis and Prediction Dashboard  

### Overview  
a comprehensive **Streamlit based dashboard** designed for stock analysis  prediction  and technical evaluation.  

Streamlit App Link : https://stock-analysis-and-price-prediction-app.streamlit.app/

![image](https://github.com/user-attachments/assets/ec709f1a-6a7e-4e60-a629-76aa0ebd813b)
![image](https://github.com/user-attachments/assets/146fa83d-1f5f-42c6-942f-5e36d4d35ccc)

---

### Features  
- **Stock Statistics**:  
  - Explore current and historical stock data, including price trends, RSI, ATR, and volume metrics.  
  - View advanced statistics such as moving averages, volatility, and price ranges.  

- **Technical Analysis**:  
  - Dynamic candlestick charts with overlays of key indicators like MA, Bollinger Bands, MACD, and more.  
  - Visualize detailed RSI and MACD trends for deeper insights into market movements.  

- **Price Prediction**:  
  - Leverages **Random Forest Regression** for predicting future stock prices.  
  - Provides key metrics like RMSE and prediction accuracy for evaluating the model’s performance.  

- **Seamless Navigation**:  
  - Switch  between statistics and analysis or  prediction modules with a responsive and intuitive interface.  

---

### How to Use  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/momentumai-quant/Streamlit-Stock-Analysis-and-Price-Prediction-App 
   cd Streamlit-Stock-Analysis-and-Price-Prediction-App   
   ```  

2. **Install Dependencies**  
   Ensure you have Python 3.8+ installed, then run:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the App**  
   ```bash  
   streamlit run app.py  
   ```  

4. **Explore the Features**  
   - Input stock symbols like `AAPL`, `GOOGL`, or `BTC-USD`.  
   - Analyze detailed stock statistics and visualize trends.  
   - Predict future prices and compare with actual values.  

---

### Technical Highlights  
- **Libraries Used**:  
  - Data Analysis: Pandas, NumPy, Scikit-learn  
  - Visualization: Plotly, Matplotlib, Seaborn  
  - Machine Learning: Random Forest for regression-based predictions  

- **Key Indicators**:  
  - Moving Averages (MA9, MA13, MA20, MA30)  
  - RSI (Relative Strength Index)  
  - MACD (Moving Average Convergence Divergence)  
  - ATR (Average True Range)  

 
 
