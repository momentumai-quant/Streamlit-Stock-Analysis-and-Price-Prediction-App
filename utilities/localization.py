from typing import Dict, Literal
from dataclasses import dataclass

@dataclass
class LocalizationConfig:
    def __init__(self,lang='en'):
        self.current_language: Literal['en', 'fa'] = lang
        self._translations: Dict[str, Dict[str, str]] = {
            #dashbaord
            'dashboard_title': {
                'en': 'Stock Analysis Dashboard',
                'fa': 'داشبورد تحلیل سهام'
            },
            'language_selector': {
                'en': 'زبان فارسی',
                'fa': 'English Language'
            },
            
            #nav bar buttons
            'nav_stock_statistics': {
                'en': 'Stock Statistics',
                'fa': 'اطلاعات کلی سهام'
            },
            'nav_analysis': {
                'en': 'Market Analysis (Indicators)',
                'fa': 'تحلیل بازار - اندیکاتور ها'
            },
            'nav_prediction': {
                'en': 'Price Prediction',
                'fa': 'پیش‌بینی قیمت'
            },

            #top bar 
            'config': {
                'en': 'Configuration',
                'fa': 'تنظیمات'
            },
            'symbol': {
                'en': 'Stock Symbol:',
                'fa': 'نماد سهام:'
            },
            'period': {
                'en': 'Time Period:',
                'fa': 'بازه زمانی:'
            },
            'prediction_days': {
                'en': 'Prediction Days',
                'fa': 'روزهای پیش‌بینی'
            },
            'analyze_button': {
                'en': 'Analyze',
                'fa': 'تحلیل'
            },

            #indicators 
            'price_movement': {
                'en': 'Price Movement',
                'fa': 'نمودار قیمت'
            },
            'technical_indicators': {
                'en': 'Technical Indicators',
                'fa': 'اندیکاتورهای تکنیکال'
            },
            'rsi_indicator': {
                'en': 'Relative Strength Index (RSI)',
                'fa': 'شاخص قدرت نسبی (RSI)'
            },
            'macd_indicator': {
                'en': 'Moving Average Convergence Divergence (MACD)',
                'fa': 'واگرایی میانگین متحرک (MACD)'
            },
            'atr_indicator': {
                'en': 'Average True Range (ATR)',
                'fa': 'میانگین دامنه واقعی (ATR)'
            },
            'bollinger_bands': {
                'en': 'Bollinger Bands',
                'fa': 'باندهای بولینگر'
            },

            #analysis
            
            'price_stats': {
                'en': 'Price Statistics',
                'fa': ' قیمت'
            },
            'volume_analysis': {
                'en': 'Volume Analysis',
                'fa': ' حجم'
            },
            'correlation_analysis': {
                'en': 'Correlation Analysis',
                'fa': 'تحلیل همبستگی'
            },
            'feature_importance': {
                'en': 'Feature Importance',
                'fa': 'اهمیت ویژگی‌ها'
            },
            'trend_analysis': {
                'en': 'Trend Analysis',
                'fa': 'تحلیل روند'
            },

            "current_rsi":{
                "en":"RSI",
                "fa":"RSI",
            },

            'highest_price': {
                'en': 'Highest Price:',
                'fa': 'بالاترین قیمت:'
            },
            'lowest_price': {
                'en': 'Lowest Price:',
                'fa': 'پایین‌ترین قیمت:'
            },
            'average_price': {
                'en': 'Average Price:',
                'fa': 'میانگین قیمت:'
            },
            'price_volatility': {
                'en': 'Price Volatility:',
                'fa': 'نوسان قیمت:'
            },

            
            'average_volume': {
                'en': 'Average Volume:',
                'fa': 'میانگین حجم:'
            },
            'max_volume': {
                'en': 'Maximum Volume:',
                'fa': 'حداکثر حجم:'
            },
            'min_volume': {
                'en': 'Minimum Volume:',
                'fa': 'حداقل حجم:'
            },
            'volume_trend': {
                'en': 'Volume Trend:',
                'fa': 'روند حجم:'
            },
            'ma_signal': {
                "en":"Moving Avg Signal",
                "fa":"سیگنال میانگین متحرک"
            },
            'macd_signal':{
                "en":"MACD Signal",
                "fa":"سیگنال MACD"
            },

            #prediction
            'price_prediction': {
                'en': 'Price Prediction',
                'fa': 'پیش‌بینی قیمت'
            },
            'prediction_metrics': {
                'en': 'Prediction Metrics',
                'fa': 'معیارهای پیش‌بینی'
            },
            'prediction_rmse': {
                'en': 'Prediction RMSE',
                'fa': 'خطای پیش‌بینی RMSE'
            },
            'prediction_accuracy': {
                'en': 'Prediction Accuracy',
                'fa': 'دقت پیش‌بینی'
            },
            'actual_price': {
                'en': 'Actual Price',
                'fa': 'قیمت واقعی'
            },
            'predicted_price': {
                'en': 'Predicted Price',
                'fa': 'قیمت پیش‌بینی شده'
            },

            #timeframes
            'time_periods': { 
                '6mo': {'en': '6mo', 'fa': '6mo'},
                '1y': {'en': '1y', 'fa': '1y'},
                '2y': {'en': '2y', 'fa': '2y'},
                '5y': {'en': '5y', 'fa': '5y'}
            },

            #trends
            'increasing': {
                'en': 'Increasing',
                'fa': 'افزایشی'
            },
            'decreasing': {
                'en': 'Decreasing',
                'fa': 'کاهشی'
            },
            'bullish': {
                'en': 'Bullish',
                'fa': 'صعودی'
            },
            'bearish': {
                'en': 'Bearish',
                'fa': 'نزولی'
            },

            #messages
            'loading': {
                'en': 'Loading and analyzing data...',
                'fa': 'در حال دریافت و تحلیل اطلاعات...'
            },
            'error_fetching': {
                'en': 'Error fetching data:',
                'fa': 'خطا در دریافت اطلاعات:'
            },
            'analysis_ready':{
                "en":"Technical Analysis is Ready ! please Go To Anlysis Tab",
                "fa":"نمودار های تحلیل تکنیکال میتوانید اکنون از تب تحلیل تگنیکال ببینید"
            },
            "symbol_search":{
                "en": "You Can Find More Symbols From Yahoo Finance(BTC-USD , AAPL )",
                "fa": "You Can Find More Symbols From Yahoo Finance(BTC-USD , AAPL )",

            }

        }

    def get_text(self, key: str, subkey: str = None) -> str: 
        if subkey:
            return self._translations.get(key, {}).get(subkey, {}).get(
                self.current_language,
              {}
            )
        return self._translations.get(key, {}).get(
            self.current_language,
             {}
        )
    def get_subkeys(self,key)-> list:
         return list(self._translations.get(key,{}).keys())
    def switch_language(self) -> None: 
        print("language changed from ",self.current_language)
        if self.current_language =="en":
            self.current_language = 'fa'
        else :
            self.current_language == 'en'
        print("language changed to ",self.current_language)

    def get_time_period_text(self, period_key: str) -> str: 
        return self._translations['time_periods'].get(period_key, {}).get(
            self.current_language,
            period_key
        )