# Importing required libraries
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import datetime as dt1
from datetime import datetime as dt
import quandl
import datetime
import scipy
import pandas as pd
# Getting the google dataset
# and store it in the variable 'df'
#API_KEY = str(open('./../API.txt').read()).replace('\n', '')
#df = quandl.get("WIKI/GOOG", api_key=API_KEY)
#df=pd.read_csv("29-06-2016-TO-28-06-2018INFYALLN.csv")
df=quandl.get("NSE/TCS")
print(df.tail())
# We are gonna use Adj. Close in order to predict the stock
df = df[['Close']]
print(df)
# forecast_out variable is keeping track of how many days into the future we want to predict
forecast_out = int(30) # 30 days into the future
df['Prediction'] = df[['Close']].shift(-forecast_out)

# printing a plot to show the evolution of Google stock in time
df['Close'].plot(figsize=(15, 6), color="green")
# creating the labels 
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
X = np.array(df.drop(['Prediction'], 1))
# scaling our features to normalize data
X = preprocessing.scale(X)
print(X)
X_forecast = X[-forecast_out:] # set X_forecast equal to last 30
X = X[:-forecast_out] # remove last 30 from X

# y is going to be our prediction array 
Y = np.array(df['Prediction'])
Y = Y[:-forecast_out]
print(Y)
# we take 20% of the train data and use it for prediction
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2)

# LINEAR REGRESSION 
# Training our algorithm
clf = LinearRegression()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)
print("Accuracy: ", accuracy)
# showing the last 30 days
forecast_prediction = clf.predict(X_forecast)
print(forecast_prediction)
# Ploting the predicted prices
df.dropna(inplace=True)
# initialiseing a new column called forecast with nan
df['forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

print('Last date: ',last_date)
# print('Last unix: ', last_unix)


# adding predictions to the data frame to create the next 30 days
for i in forecast_prediction:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]

df['Close'].plot(figsize=(15,6), color="green")
df['forecast'].plot(figsize=(15,6), color="red")
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
# SUPORT VECTOR MACHINE PREDICTION

# initialising lists used for prediction
prices = []
dates = []

# getting data frame
df = quandl.get("NSE/TCS")
# selecting only the features I would need 
df = df[['Close']]
df = df.reset_index()

# print(df['Date'].dt.days)
#print(df['Date'])
# print('After conversion')
# for row in df['Date']:
#     print(np.datetime64(row))
#     dt64 = np.datetime64(row)
#     ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
#     print(ts)

# interate over rows in pandas
# row[0] - date
# row[1] - price
# scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
for _, row in df.iterrows():
    #dates.append(int(str(row[0]).split('-')[2].split(' ')[0]))
    dt64 = np.datetime64(row[0])
    # switch to hours
    ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 'D')
    print(ts)
    #print(ts)np.timedelta64(1, 's')
    dates.append(ts)
    prices.append(float(row[1]))


# normalizing data
#dates = [number/scipy.linalg.norm(dates) for number in dates]

print(dates)
# print(dates)
# print(prices)
# svr_lin = SVR(kernel='linear', C=1e3)
# svr_poly = SVR(kernel='poly', C=1e3, degree=2)
# svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

# # SV needs a 2D array so I am converting the 1D data to 2D 
# dates = np.reshape(dates, (len(dates), 1))


# # start fiting
# svr_rbf.fit(dates, prices) 
# svr_lin.fit(dates, prices)
# svr_poly.fit(dates, prices)


# plt.scatter(dates, prices, color= 'black', label= 'Data')
# # plotting the line made by the RBF kernel
# plt.plot(dates, svr_rbf.predict(dates), color= 'red', label= 'RBF model')
# # plotting the line made by linear kernel
# plt.plot(dates,svr_lin.predict(dates), color= 'green', label= 'Linear model') 
#  # plotting the line made by polynomial kernel
# plt.plot(dates,svr_poly.predict(dates), color= 'blue', label= 'Polynomial model')
# plt.xlabel('Date') 
# plt.ylabel('Price')
# plt.title('Support Vector Regression') 
# plt.legend() 
# plt.show()

# day = 0
# print('SVR RBF: ', svr_rbf.predict(day)[0])
# print('SVR LIN: ',svr_lin.predict(day)[0])
# print('SVR POLY: ', svr_poly.predict(day)[0])
# Getting data 
# extracting Features

df = quandl.get("NSE/TCS")
print('Before:')
print(df)
df = df[['Open','High','Low','Close']]
df['HL_PCT']= (df['High'] - df['Close']) / df['Close'] *100
df['PCT_change']= (df['High']-df['Open']) / df['Open'] *100
df=df[['Close','HL_PCT','PCT_change']]
df.head(3)
print('After:')
print(df)
# Processing data
import math
forecast_col = 'Close'
#no na in data but good practice
df.fillna(-99999, inplace=True)

# I switched to 7 days this time
n=7 #
forecast_out = int(math.ceil(n)) #make n integer

df['label'] = df[forecast_col].shift(+forecast_out)
print(df)
# extracting features

import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately= X[-forecast_out:] #shift the most recent data (e.g. 95-100)
X = X[:-forecast_out] #shift data until beginning of X_lately (e.g. 0-94)
#print(X, len(X))

df.dropna(inplace=True)
y = np.array(df['label'])
#print(len(X)==len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
# applying  the algorithmm
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

# measuring accuracy
accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)
# From prev week
accuracy = clf.score(X_test[-10:],y_test[-10:])
print('Accuracy:', accuracy)
# Switching to ensemble learning -> RandomForestRegressor
clf = RandomForestRegressor()
clf.fit(X_train, y_train)

# I observed that the accuracy was decreassing
accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)
import math
import pandas as pd
import numpy as np

from sklearn import preprocessing, cross_validation, cross_decomposition
from sklearn.linear_model import LinearRegression as LR
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor as NR
from sklearn.tree import DecisionTreeRegressor as DR
from sklearn.ensemble import RandomForestRegressor as RR

# creating a list of regressors
regressors = [LR(), SVR(), NR(), DR(), RR()]
# storing accuracy to plot it
accuracy = []
# storing prediction
forecast = []

for regressor in regressors:
    # fitting the regressor
    regressor.fit(X_train, y_train)
    # getting the score
    a = regressor.score(X_test, y_test)
    print('Accuracy of ',str(regressor)[:3], ' is: ', a)
    accuracy.append(a)
    forecast.append(regressor.predict(X_lately))
    
import matplotlib.pyplot as plt
from matplotlib import style
#%matplotlib inline
import datetime as dt

last_date=df.index[-1]
#print last_date
next_date= last_date + dt.timedelta(days=1)
#print next_date

dates=[]
for i in range(n): #add 7 days
    next_date= last_date + dt.timedelta(days=i)
    dates.append(next_date)

colors=['r','b','g','m', 'y']
for j in range(len(forecast)):
    plt.plot(dates, forecast[j], '-', color=colors[j], label='{0}: {1:.2f}'.format(str(regressors[j])[:3], accuracy[j]));
plt.xticks(rotation=45)
plt.legend(loc='best') #bottom right
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('$n$=7 days prediction of TCS stocks market using various regressors')
plt.show()
