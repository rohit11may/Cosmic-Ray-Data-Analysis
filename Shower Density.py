#density of showers

import numpy as np
import matplotlib.pyplot as plt
import os
import inspect
from datetime import datetime

fileName = "\\0.1.1_07_2011-22_01_2012_allCSV.txt"

tempFilePath = (os.path.abspath(os.path.join(inspect.getfile(inspect.currentframe()), os.pardir))).split("\\")
fileVar = open("\\".join(tempFilePath[0:len(tempFilePath)-1]) + fileName)

density = []
dateStr = fileVar.readline().split(',')[0:2]
print(dateStr)
dateStr = dateStr[0] + ',' + dateStr[1][0:2]
currentdate_object = datetime.strptime(dateStr, '%Y/%m/%d,%H')
count = 1
for x in fileVar:
	y  = x.split(',')
	dateStr = y[0] + ',' + y[1][0:2]
	newdate_object = datetime.strptime(dateStr, '%Y/%m/%d,%H')
	if newdate_object == currentdate_object:
		count += 1
	else:
		density.append({currentdate_object: count})
		currentdate_object = newdate_object
		count = 1

for z in density:
	print(z)
