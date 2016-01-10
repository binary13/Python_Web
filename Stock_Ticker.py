import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np
import datetime as dt

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    plt.xlabel('Date')
    plt.ylabel('Price')

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

    # date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
    #                                                       delimiter=',',
    #                                                       unpack=True)
    #
    # date_conv = np.vectorize(dt.datetime.fromtimestamp)
    # date = date_conv(date)


    ax1.plot_date(date, closep, '-')
    ax1.fill_between(date, closep, 70, where=(closep >= 70), facecolor='g', alpha=0.8)
    ax1.fill_between(date, closep, 70, where=(closep <= 70), facecolor='r', alpha=0.8)
    ax1.grid(True)
    ax1.yaxis.label.set_color('m')
    ax1.xaxis.label.set_color('c')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)


    plt.subplots_adjust(left=.09, bottom=.16, right=.94, top=.95, wspace=.2, hspace=.2)
    plt.show()

stock = 'xom'            ###input('Stock to plot: ')
graph_data(stock)