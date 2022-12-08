from config import key
import requests
import csv
from datetime import datetime
import time

# This is a list of stock tickers of the companies we are getting data for 
stocks = ["AAPL", "WMT","AMZN", "NFLX", "PYPL"]

def getPolygonData(stock):
    '''
    The function receives a stock name and uses it to make a request for the specific data for that stock using API
    The data is filtered, the function only collects date and a closing price of a stock for the specified in the API call date range

    Parameters
    ----------
    stock: string
        Name of a stock

    Returns
    -------
    dict
        A dictionary, where date serves as a key, closing price as a value. The number of items in dictionary is equivalent
        to the number of items we received through API request.

    '''
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock}/range/1/day/2021-03-29/2022-03-25?adjusted=true&limit=300&apiKey={key}"
    data = requests.get(url)
    fin_data = data.json()
    # the info we are looking for is stored in the dictionary with the key "results"
    results = fin_data["results"]
    #using list comprehension we are getting 2 lists -> closing prices and dates these closings occured
    close_price = [n['c'] for n in results]
    date = [time.strftime('%Y-%m-%d', time.localtime(day['t']/1000)) for day in results]
    #creating a dictionary with dates keys and closing prices values
    date_price = dict(zip(date,close_price))
    return date_price


def createFile(date_price, name):
    '''
    The function stores stock data into a scv file into Stocks folder
    
    Parameters
    ----------
    date-price: dictionary
        Dictionary contains date:price key value pairs
    name: string
        The parameter gives us a ticker name for a company, so we can save a file with an appropriate name

    Output: scv file
        A file is created,it contains dates and closing prices of a stock
    '''
    #the names of the data header
    csv_columns = ["DATE","PRICE"]
    with open (f"Stocks/{name}.csv", "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames = csv_columns)
        writer.writeheader()
        #saving the data received as a parameter into a file
        #had to use for loop to write data into a file
        for key in date_price.keys():
            outfile.write("%s,%s\n"%(key, date_price[key]))
                
#with the list comprehension calling the function getPolygonData to collect data for all stocks we are analyzing
#the variable date_priceAll will store a list of dictionaries
date_priceAll = [getPolygonData(s) for s in stocks]

#calling createFile function in order to write and save file for each analyzed company
for (d,n) in zip (date_priceAll, stocks) :
    createFile(d,n)

