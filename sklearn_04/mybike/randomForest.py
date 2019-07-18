
import csv
from math import log, exp
 
import numpy
from sklearn.ensemble import RandomForestRegressor
 
 
from datetime import datetime
 
import pandas
 
 
def parse_time(data):
	date = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
	hour = date.hour
	day = date.day
	month = date.month
	dow = date.weekday()
	year = date.year
	return year, month, day, hour, dow
 
 
def mylog(data):
	data = int(data) + 1
	return log(data)
 
 
dataset = pandas.read_csv("train.csv")
testset = pandas.read_csv("test.csv")
 
labelData = dataset['casual'].apply(func=mylog).values
labelData2 = dataset['registered'].apply(func=mylog).values
myIndex = testset['datetime']
 
feature1 = ['atemp', 'temp', 'hour', 'humidity', 'windspeed',
			'month', 'dow', 'workingday', 'holiday', 'year', 'weather']
 
# datetime
dataset['year'], dataset['month'], dataset['day'], dataset['hour'], dataset['dow'] = zip(
	*dataset['datetime'].apply(func=parse_time))
testset['year'], testset['month'], testset['day'], testset['hour'], testset['dow'] = zip(
	*testset['datetime'].apply(func=parse_time))
 
trainData = dataset[feature1].iloc[:, :].values
testData = testset[feature1].iloc[:, :].values
 
rfModel = RandomForestRegressor(n_estimators=100)
rfModel.fit(trainData, labelData)
preds = rfModel.predict(testData).tolist()
preds = [exp(i) - 1 for i in preds]
 
 
# registered ================================================
feature2 = ['hour', 'humidity', 'atemp', 'temp', 'windspeed',
			'month', 'dow', 'workingday', 'holiday', 'year', 'weather']
trainData = dataset[list(feature2)].iloc[:, :].values
testData = testset[list(feature2)].iloc[:, :].values
 
rfModel = RandomForestRegressor(n_estimators=100)
rfModel.fit(trainData, labelData2)
preds2 = rfModel.predict(testData).tolist()
preds2 = [exp(i) - 1 for i in preds2]
 
 
# ==================================================================
 
preds = numpy.column_stack((myIndex, map(lambda x, y: x + y, preds, preds2))).tolist()
 
with open("sub_rf.csv", "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerow(["datetime", "count"])
	writer.writerows(preds)