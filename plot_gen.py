import pandas as pd
import mplfinance as mpf
import threading
import matplotlib.animation as animation
import datetime
from datetime import date, datetime


# fig = mpf.figure(style="checkers", figsize=(6, 7))
# ax1 = fig.add_subplot(1, 1, 1)

# def genPlot():
#    threading.Timer(10.0, genPlot).start()
idf = pd.read_csv("bitcoin_data_tut.csv")
idf['minute'] = pd.to_datetime(idf['minute'], format="%m/%d/%Y %H:%M")
idf.set_index('minute', inplace=True)
save = dict(fname='t30.png', dpi=100, pad_inches=0.25, transparent=True)
mpf.plot(idf, type='candle', style='checkers', mav=(3, 6, 9), ylabel='BTC / USD', savefig=save)

saveTmp = dict(fname='/tmp/btc_chart.png', dpi=90, pad_inches=0.25, transparent=True)
mpf.plot(idf, type='candle', style='mike', ylabel='BTC / USD', savefig=saveTmp)


idf = pd.read_csv("bitcoin_data_tut.csv")
idf['minute'] = pd.to_datetime(idf['minute'], format="%m/%d/%Y %H:%M")
idf.set_index('minute', inplace=True)
saveTmp = dict(fname='/tmp/btc_chart_day.png', dpi=90, pad_inches=0.25, transparent=False)
mpf.plot(idf, type='line', style='mike', mav=(3, 6, 9), ylabel='BTC / USD', savefig=saveTmp)

# genPlot()
