!pip install gradio yfinance -q

import gradio as gr
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def analyze_oil(ticker_symbol):
    if not ticker_symbol:
        return "الرجاء إدخال رمز", None
    try:
        # جلب البيانات
        data = yf.download(ticker_symbol, period="1y")
        
        # رسم الرسم البياني
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(data.index, data['Close'], color='purple')
        ax.set_title(f"سعر الإغلاق لـ {ticker_symbol}")
        ax.set_xlabel("التاريخ")
        ax.set_ylabel("السعر (USD)")
        ax.grid(True)
        
        # حساب إحصائيات
        max_price = data['Close'].max().item()
        min_price = data['Close'].min().item()
        avg_price = data['Close'].mean().item()
        
        report = f"📊 تحليل {ticker_symbol}:\n"
        report += f"- أعلى سعر: ${max_price:.2f}\n"
        report += f"- أدنى سعر: ${min_price:.2f}\n"
        report += f"- متوسط السعر: ${avg_price:.2f}\n"
        
        return report, fig # نرجع الرسم البياني مباشرة
    except Exception as e:
        return f"حدث خطأ: {e}", None

app = gr.Interface(
    fn=analyze_oil,
    inputs=gr.Textbox(label="أدخل رمز النفط (مثلاً: CL=F)"),
    outputs=[gr.Textbox(label="التقرير"), gr.Plot(label="الرسم البياني")], # التغيير هنا: gr.Plot
    title="🛢️ المحلل الذكي لأسعار النفط",
    description="أداة ذكاء اصطناعي لتحليل بيانات أسعار النفط."
)

app.launch(share=True, debug=False)
