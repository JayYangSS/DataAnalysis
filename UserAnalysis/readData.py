import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt 
from pandas.tools.plotting import scatter_matrix
import sys,os
import json


# split the big json file into several small csv files
def getCSV(todir='data\\splitData\\meeting_data'):
	if not os.path.exists(todir):
		print('path does not exist')
	else:
		for fname in os.listdir(todir):
			focus_data=DataRead(todir+'\\'+fname)
			focus_data.readMSJson()
			focus_data.getDataFrame()
			strList=fname.split('.')
			focus_data.dataFrame.to_csv(strList[0]+'.csv')


class DataRead(object):
	"""docstring for DataRead"""
	def __init__(self, path):
		super(DataRead, self).__init__()
		self.path = path
		self.data={}
		self.dataFrame={}

	#get the DataFrame 
	def getDataFrame(self):
		dataFrame=pd.read_json(self.data)
		self.dataFrame=dataFrame


	#get the json from json file
	def readMSJson(self):
		for line in open(self.path):
			lineStr=line.split(': {')
			userHash=lineStr[0]
			jsonVal='{'+lineStr[1]

			jsonData=json.loads(jsonVal)#return type is `dict`
			self.data[userHash]=jsonData
		self.data=json.dumps(self.data)


	# dayAverage=True,return the average time of all stuff in one day
	# else, return the average time of a stuff with all days 
	def getAverageTime(self,dayAverage=True):
		dataFrame=self.dataFrame.T
		if dayAverage:
			return dataFrame.mean()
		else:
			return dataFrame.mean(axis=1)

	def getDiffFeature(self):
		dataFrame=self.dataFrame
		diff=dataFrame.diff()
		print(diff)
		diff[-50:].plot()
		plt.show()

	

	def HistPlot(self,figureId):
		dataFrameForHist=self.dataFrame.T

		fig=plt.figure(figureId)
		# plt.title()

		subPic1=fig.add_subplot(331)
		subPic1.set_title('Hist of 2016-04-26')
		dataFrameForHist['2016-04-26'].plot.hist()
		subPic1=fig.add_subplot(332)
		subPic1.set_title('Hist of 2016-04-27')
		dataFrameForHist['2016-04-27'].plot.hist()
		subPic1=fig.add_subplot(333)
		subPic1.set_title('Hist of 2016-04-28')
		dataFrameForHist['2016-04-28'].plot.hist()
		subPic1=fig.add_subplot(334)
		subPic1.set_title('Hist of 2016-04-29')
		dataFrameForHist['2016-04-29'].plot.hist()
		subPic1=fig.add_subplot(335)
		subPic1.set_title('Hist of 2016-04-30')
		dataFrameForHist['2016-04-30'].plot.hist()
		subPic1=fig.add_subplot(336)
		subPic1.set_title('Hist of 2016-05-01')
		dataFrameForHist['2016-05-01'].plot.hist()
		subPic1=fig.add_subplot(337)
		subPic1.set_title('Hist of 2016-05-02')
		dataFrameForHist['2016-05-02'].plot.hist()
		subPic1=fig.add_subplot(338)
		subPic1.set_title('Hist of 2016-05-03')
		dataFrameForHist['2016-05-03'].plot.hist()
		subPic1=fig.add_subplot(339)
		subPic1.set_title('Hist of 2016-05-04')
		dataFrameForHist['2016-05-04'].plot.hist()


		fig=plt.figure(figureId+1)
		subPic1=fig.add_subplot(331)
		subPic1.set_title('Hist of 2016-05-05')
		dataFrameForHist['2016-05-05'].plot.hist()
		subPic1=fig.add_subplot(332)
		subPic1.set_title('Hist of 2016-05-06')
		dataFrameForHist['2016-05-06'].plot.hist()
		subPic1=fig.add_subplot(333)
		subPic1.set_title('Hist of 2016-05-07')
		dataFrameForHist['2016-05-07'].plot.hist()
		subPic1=fig.add_subplot(334)
		subPic1.set_title('Hist of 2016-05-08')
		dataFrameForHist['2016-05-08'].plot.hist()
		subPic1=fig.add_subplot(335)
		subPic1.set_title('Hist of 2016-05-09')
		dataFrameForHist['2016-05-09'].plot.hist()
		subPic1=fig.add_subplot(336)
		subPic1.set_title('Hist of 2016-05-10')
		dataFrameForHist['2016-05-10'].plot.hist()
		subPic1=fig.add_subplot(337)
		subPic1.set_title('Hist of 2016-05-11')
		dataFrameForHist['2016-05-11'].plot.hist()
		subPic1=fig.add_subplot(338)
		subPic1.set_title('Hist of 2016-05-12')
		dataFrameForHist['2016-05-12'].plot.hist()
		subPic1=fig.add_subplot(339)
		subPic1.set_title('Hist of 2016-05-13')
		dataFrameForHist['2016-05-13'].plot.hist()
		
	
	def percentChange(self,name):
		data=self.dataFrame.T
		
		#get the specified person data
		personData=data.loc[name]
		fig=plt.figure(9)

		# get the percent change in everyday
		subPic1=fig.add_subplot(121)
		subPic1.set_title('percent change in everyday')
		personData.pct_change().plot(kind='bar')


		# get the percent change (period=7)
		subPic2=fig.add_subplot(122)
		subPic2.set_title('percent change (period=7)')
		personData.pct_change(periods=7).plot(kind='bar')


	#  get the workday workline and average work line in every work day
	def SpecifiedPersonWorkLine(self,name):
		data=self.dataFrame.T
		
		#get the specified person data
		personData=data.loc[name]
		fig=plt.figure(8)
		
		# calculate the workday data
		averageWeekDay=[]
		varianceWeekDay=[]
		weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
		for x in range(5):
			subPic1=fig.add_subplot(331+x)
			subPic1.set_title(weekdays[x])
			#print(personData[personData.index.weekday==x])
			weekdayData=personData[personData.index.weekday==x]
			weekdayData.plot(kind='bar')
			varianceWeekDay.append(weekdayData.var())
			averageWeekDay.append(weekdayData.mean())
			

		subPic1=fig.add_subplot(336)
		subPic1.set_title('work line')
		personData.plot(kind='bar')

		# plot average work time on every workday
		subPic1=fig.add_subplot(337)
		subPic1.set_title('average WeekDay')
		averageWeekDaySeries=pd.Series(data=averageWeekDay,index=weekdays[:5])
		averageWeekDaySeries.plot()

		subPic1=fig.add_subplot(339)
		subPic1.set_title('variance of weekdays')
		varianceWeekDaySeries=pd.Series(data=varianceWeekDay,index=weekdays[:5])
		varianceWeekDaySeries.plot()

		# get 1-order diff of a person
		subPic1=fig.add_subplot(338)
		subPic1.set_title('first order diff')
		diff1=personData.diff()
		diff1.plot(kind='bar')


		subPic1=fig.add_subplot(339)
		subPic1.set_title('second order diff')
		diff2=diff1.diff()
		diff2.plot(kind='bar')

		# plt.ylim((0,600))
		# print(personData.index.weekday)


		# print(data)

	# def plotTest(self):
	# 	#get the user data,dataType:Series
	# 	user1=self.dataFrame['"549b973dbd2b6fb6d0f5ee855d63a1d5e5f0b7dc2cc9ab4a6b1eb633"']
	# 	user2=self.dataFrame['"8a6249e51a0647c6b5aee59ffb6fa623f473557cde8fe2e8aafa25d2"']
	# 	user3=self.dataFrame['"aa4b0f37c7b806c6aff563fe687560180e3ff3cfd4f2b25a85dec551"']
	# 	user4=self.dataFrame['"16d2192b844c2c1b28f5b7aaf11144c851ed08606ccf43dff55f629a"']
	# 	#plot
	# 	plt.subplot(221)
	# 	user1.plot(kind='bar',title='Focus Time')
	# 	plt.subplot(222)
	# 	user2.plot(kind='bar',title='Focus Time')
	# 	plt.subplot(223)
	# 	user3.plot(kind='bar',title='Focus Time')
	# 	plt.subplot(224)
	# 	user4.plot(kind='bar',title='Focus Time')
	# 	plt.show()
		

	def plotTest2(self):
		#get the user data,dataType:Series
		self.dataFrame.plot()
		plt.show()

if __name__ == '__main__':

	focus_path=r'data\\splitData\\focus_data1000\\total_focus1.json'
	# focus_path=r'data\\total_focus.json'
	# meeting_path=r'data\\total_meeting.json'
	meeting_path=r'data\\splitData\\meeting_data1000\\total_meeting1.json'
	focus_data=DataRead(focus_path)
	focus_data.readMSJson()
	focus_data.getDataFrame()
	focusDataFrame=focus_data.dataFrame.T


	#focus_data.getDiffFeature()
	dayAverage=focus_data.getAverageTime()
	fig=plt.figure(1)
	pic1=fig.add_subplot(121)
	pic1.set_title('Average focus time everyday')
	personAverage=focus_data.getAverageTime(dayAverage=False)
	dayAverage.plot(grid=True)
	dayAverage.diff().plot(grid=True,secondary_y=True,style='g')


	pic2=fig.add_subplot(122)
	pic2.set_title('Average focus time everyPerson')
	personAverage.plot(grid=True)
	#personAverage.diff().plot()



	# focus_data.plotTest2()
	# focus_data.dataFrame.to_csv('total_focus.csv')
	meeting_data=DataRead(meeting_path)
	meeting_data.readMSJson()
	meeting_data.getDataFrame()
	meetingDataFrame=meeting_data.dataFrame.T

	meetingDayAverage=meeting_data.getAverageTime()
	fig=plt.figure(2)
	pic1=fig.add_subplot(121)
	pic1.set_title('Average meeting time everyday')
	personAverageMeeting=meeting_data.getAverageTime(dayAverage=False)
	meetingDayAverage[-28:].plot(grid=True)


	pic2=fig.add_subplot(122)
	pic2.set_title('Average meeting time everyPerson')
	personAverageMeeting.plot(grid=True)
	#personAverageMeeting.diff().plot()
	

	# meeting_data.HistPlot(figureId=3)
	# focus_data.HistPlot(figureId=5)
	focus_data.SpecifiedPersonWorkLine(name='"2cfc64076b4aab8f1b34acec149265c04a6ec63abde1753a0a2ad66b"')
	# meeting_data.SpecifiedPersonWorkLine(name='"2cfc64076b4aab8f1b34acec149265c04a6ec63abde1753a0a2ad66b"')

	#calculate the variance
	focusVariance=focus_data.dataFrame.var()
	focusVariance.to_csv('focusVariance.csv')

	# get the pecent change
	focus_data.percentChange(name='"2cfc64076b4aab8f1b34acec149265c04a6ec63abde1753a0a2ad66b"')

	#meeting_data.dataFrame.to_csv('total_meeting.csv')
	
	#pd.DataFrame.merge(focusDataFrame,how='left',)




	##TODO: using pct_change to get the percent change

	##TODO: meeting and focus time scatter_matrix
	# scatter_matrix(focus_data.dataFrame,diagonal='kde')
	plt.show()