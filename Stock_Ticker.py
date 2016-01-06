import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np

def graph_data(stock):
    print('Currently pulling: ', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    source_split = source_code.split('\n')

    for line in source_split:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values:Date' not in split_line:
                stock_data.append(split_line)

    for d in stock_data:
        print(d)

stock = input('Stock to plot: ')
graph_data(stock)