import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import urllib
import numpy as np
import datetime as dt

def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    plt.xlabel('Date')
    plt.ylabel('Price')

    print('Currently pulling: ', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1' \
                                                                    'm/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    source_split = source_code.split('\n')

    for each_line in source_split:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    def unpack(source):
        # For datetime: when charting more than 1d
        if 'values:Date' in source:
            print("Date found")
            return np.loadtxt(stock_data,
                              delimiter=',',
                              unpack=True,
                              converters={0: mdates.bytespdate2num('%Y%m%d')})

        # For Unix time codes: when charting 1d
        elif 'values:Time' in source:
            print("Time found")
            date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                                  delimiter=',',
                                                                  unpack=True)
            date_conv = np.vectorize(dt.datetime.fromtimestamp)
            date = date_conv(date)
            return date, closep, highp, lowp, openp, volume
        else: return "Date or Time not found"

    date, closep, highp, lowp, openp, volume = unpack(source_code)

    x = 0
    y = len(date)
    new_list = []

    for x in range(y):
        append_line = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        new_list.append(append_line)


    # ax1.plot_date(date, closep, '-')

    candlestick_ohlc(ax1, new_list, width=.8, colorup='g', colordown='r')

    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.grid(True)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.subplots_adjust(left=.09, bottom=.20, right=.94, top=.95, wspace=.2, hspace=.2)
    plt.show()

stock = 'xom'            ###input('Stock to plot: ') ### Hardcoded to avoid having to type in a symbol each run
graph_data(stock)