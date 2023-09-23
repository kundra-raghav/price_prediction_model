'''import pandas
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression


data = pandas.read_csv('iphone_price.csv')
plot.scatter(data['version'] , data ['price'])
plot.show()

model = LinearRegression()

model.fit(data[['version']] , data[['price']])
print(model.predict([[15]])) '''

'''***from statistics import LinearRegression***'''
import pandas as pd
import matplotlib.pyplot as pt
from sklearn.linear_model import LinearRegression as lr 

data = pd.read_csv('your_data_set.csv')
pt.scatter(data['version'] , data ['price'])
pt.show()

model = LinearRegression()
model.fit(data[['version']] , data[['price']])
print(model.predict([['15']]))
