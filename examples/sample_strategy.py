import pandas as pd
import numpy as np

def moving_average_crossover(data):
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    data['Signal'] = 0
    data.loc[data['MA50'] > data['MA200'], 'Signal'] = 1
    data.loc[data['MA50'] < data['MA200'], 'Signal'] = -1
    return data

def execute_trades(data, balance=10000):
    position = 0
    for i in range(len(data)):
        if data['Signal'].iloc[i] == 1 and position == 0:
            position = balance / data['Close'].iloc[i]
        elif data['Signal'].iloc[i] == -1 and position > 0:
            balance = position * data['Close'].iloc[i]
            position = 0
    return balance
