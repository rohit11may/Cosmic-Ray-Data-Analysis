#density of showers

import numpy as np
import matplotlib.pyplot as plt
import os
import inspect
from datetime import datetime

fileName = "\\0.1.1_07_2011-22_01_2012_allCSV.txt"

tempFilePath = (os.path.abspath(os.path.join(inspect.getfile(inspect.currentframe()), os.pardir))).split("\\")
fileVar = open("\\".join(tempFilePath[0:len(tempFilePath)-1]) + fileName)

print(fileVar)
fileList = []
for x in fileVar:
	y  = x.split(',')
	dateStr = y[0] + ',' + y[1]
	date_object = datetime.strptime(dateStr, '%Y/%m/%d,%H:%M:%S')
	
