import pandas as pd
import mplfinance as mpf
import matplotlib.animation as animation
import datetime
from datetime import date, datetime

fig = mpf.figure(style="checkers", figsize=(6, 7))
ax1 = fig.add_subplot(1, 1, 1)


def animate(ival):

    idf = pd.read_csv("bitcoin_data_tut.csv", index_col=0)
    idf['minute'] = pd.to_datetime(idf['minute'], format="%m/%d/%Y %H:%M")
    idf.set_index('minute', inplace=True)

    ax1.clear
    mpf.plot(idf, ax=ax1, type='candle', style='checkers', mav=(3, 6, 9), ylabel='Price US$')


ani = animation.FuncAnimation(fig, animate, interval=10000)
mpf.show()
