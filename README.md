1. StockPerformance
The main goal of the lab is to receive stock data using Polygon API, filter it, store in csv files and analyze it.

2. Polygon API is very convenient and it's easy to create an url for the API call to get required data.
With the use of the API I collect one year of stock data for five companies. 
All we need from the received data is the closing prices and the dates.
Once the data is filtered accordinly it gets stored into csv files.
In the lab we are not only practicing writing into files, but also extracting from files using csv library. 
After extracting the data we calculate population standard deviation for each week of the data.
It allows to plot a graph with standard deviations and visualize the changes that occur with the stock prices over time. We use matplolib library to be able to graph and store the graphs as images.

3. I would love to expand this lab into a project that has user interface, where the user can specify desired company, date range, information they would like to receive regarding stock market.