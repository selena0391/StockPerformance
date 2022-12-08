import csv
import statistics
import matplotlib.pyplot as plt

def getData(name):
    '''
        The function reads data froma file and saves as a list of dictionaries

    Parameters
    ----------
    name: string
        Ticker for a stock, so we know which csv file to open from the folder Stocks

    Returns
    -------
    stock_data: list of dictinaries
        Data that is read from a file is stored as a list of dictionaries
    '''
    stock_data = []
    with open(f"Stocks/{name}.csv", "r") as infile:
        reader = csv.DictReader(infile)

        #saving stock info into list of dictionaries - date and closing price
        for row in reader:
            stock_data.append(row)

    return stock_data


def getStanDev (stock_data):
    '''
        The function receives the stock data, in particular, dates and closing prices
        It caluclates population standard deviation for each week of the data given
    
    Parameters
    ----------
        stock_data: list of dictionaries
            We receive a list of dates and closing prices, where dates and closing prices are key-value pairs

    Returns
    -------
        list:
            List of the calculated population standard deviation 

    '''
    stock_stdev = []

    i = 0
    #a list that holds a sample of data for one week of closing prices
    weeksample = []
    while i < len(stock_data):
        j = 0
        while j < 5 and i < len(stock_data):
            weeksample.append(float(stock_data[i]["PRICE"]))
            j += 1 
            i += 1
        #population standard deviation needs at least 2 values to be calculated
        #send sample to the pstdev function only with an appropriate sample size
        if len(weeksample) >= 2:
            stock_stdev.append(statistics.pstdev(weeksample))
            # after adding population standard deviation to the list, weeksample is cleared to store next week data
            weeksample = []
        else:
            continue

    return stock_stdev


def dataPlot (stock_stdev, name):
    '''
    The function is plotting a line graph with matplotlib using data points froma a list received as a parameter
    It also stores that graph as a .png file

    Parameters
    ----------
        stock_stdev: list of floats
            Population standard deviation points
        name: string
            Ticker name of a stock used to save a graph image with the correct name


    '''
    #we need to know number of weeks for the y-axis
    weeks = list(range(1,len(stock_stdev)+1))
    #the name of the graph
    plt.title(f"{name} Standard Deviation over 52 weeks")
    plt.xlabel('Weeks')
    plt.ylabel("Standard Deviation")            
    plt.plot(weeks,stock_stdev, color = "aqua")
    # method that stores a graph image into resources folder
    plt.savefig(f"resources/{name}.png")
    # plot display method
    plt.show()


stocksNames = ["AAPL", "WMT","AMZN", "NFLX", "PYPL"]
# list of lists of dictionaries, stocksData variable stores data for all the companies we are analyzing
stocksData = [getData(d) for d in stocksNames]
# list of lists, stocks_stdev variable stores population standard deviation for specified ranges for all the companies
stocks_stdev = [getStanDev(s) for s in stocksData]

#calling dataPlot function to get graphs for the analyzed companies' standard deviation changes over time
for (s,n) in zip(stocks_stdev,stocksNames):
    dataPlot(s,n)