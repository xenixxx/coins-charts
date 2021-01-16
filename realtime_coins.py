import websocket
import json
import pandas as pd
import dateutil.parser
import datetime
from datetime import date, datetime, timedelta

from pandas import DataFrame

minutes_processed = {}
minute_candlesticks = []
current_tick_btc = None
previous_tick_btc = None

socket = 'wss://ws-feed.pro.coinbase.com'
fout = 'coins_data.csv'

def on_open(ws):
    print("Connection is opened")
    subscribe_msg = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-USD", "ETH-USD"
                ]
            }

        ]
    }

    ws.send(json.dumps(subscribe_msg))


def on_message(ws, message):
    global current_tick_btc, previous_tick_btc
    global current_tick_eth, previous_tick_eth

    previous_tick_btc = current_tick_btc
    current_tick_btc = json.loads(message)

    # print(current_tick)
    print("=== Received Tick ===")

    print(message)
    print(f"{current_tick['product_ids']} @ {current_tick['price']} @ {current_tick['time']}")

    tick_datetime_object = dateutil.parser.parse(current_tick['time'])
    timenow = tick_datetime_object + timedelta(hours=1)
    tick_dt = timenow.strftime("%m/%d/%Y %H:%M")
    print(tick_datetime_object.minute)
    print(tick_dt)

    if not tick_dt in minutes_processed:
        print("This is a new candlestick")
        minutes_processed[tick_dt] = True

        if len(minute_candlesticks) > 0:
            minute_candlesticks[-1]['close'] = previous_tick['price']

        minute_candlesticks.append({
            'minute': tick_dt,
            'open': current_tick['price'],
            'high': current_tick['price'],
            'low': current_tick['price']
        })

        df: DataFrame = pd.DataFrame(minute_candlesticks[:-1])
        # with open('bitcoin_data_tut.csv', 'a') as f:
        # df.to_csv(f, header=f.tell() == 0)
        df.to_csv(fout)

    if len(minute_candlesticks) > 0:
        current_candlestick = minute_candlesticks[-1]
        if current_tick['price'] > current_candlestick['high']:
            current_candlestick['high'] = current_tick['price']
        if current_tick['price'] < current_candlestick['low']:
            current_candlestick['low'] = current_tick['price']

        print("== Candlesticks ==")
        for candlestick in minute_candlesticks:
            print(candlestick)


def on_close(ws, message):
    print("!connection_closed!")


def on_error(ws, message):
    print('!connection_error!')


ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close, on_error=on_error)
ws.run_forever()
