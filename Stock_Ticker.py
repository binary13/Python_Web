import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    print('Currently pulling: ', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    source_split = source_code.split('\n')

    for each_line in source_split:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: mdates.bytespdate2num('%Y%m%d')})

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.plot_date(date, closep, '-')
    ax1.grid(True)
    plt.show()

stock = 'aapl'            ###input('Stock to plot: ')
graph_data(stock)