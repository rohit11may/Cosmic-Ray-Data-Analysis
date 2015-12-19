_author__ = 'Rohit'
import numpy as np
import matplotlib.pyplot as plt
import os

print("running")
def constrain(minimum, maximum, small, large, val):
    ratio = (maximum - minimum) / (large - small)
    final = []
    for x in val:
        value = minimum + (ratio * (x - small))
        final.append(value)
    return final


directoryName = "G:\Computing Projects\Cosmic Rays\Summaries\A1_07_2011-22_01_2012\keyPoints"
print("1st JULY 2011 to 22nd JANUARY 2012")
totalMaxHits = [0, 0, 0]
totalMinHits = [0, 0, 0]
for fileName in os.listdir(directoryName):
    file = open(os.path.join(directoryName, fileName), 'r')
    fileL = list(file)
    maxHitStr = fileL[8][19:len(fileL[8]) - 2]
    minHitStr = fileL[9][19:len(fileL[9]) - 2]
    maxHit = [int(x.strip()[3::]) for x in maxHitStr.split(',')]
    minHit = [int(x.strip()[3::]) for x in minHitStr.split(',')]
    for x in range(3):
        totalMaxHits[x] += maxHit[x]
        totalMinHits[x] += minHit[x]
finalMax = totalMaxHits
finalMin = totalMinHits

N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, finalMax, width, color='r')
rects2 = ax.bar(ind + width, finalMin, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Total Number of Maximum Hits in a Record')
ax.set_xlabel('Detector')
ax.set_title('Strength of Hit Relative to other Detectors 01/07/11 -> 22/01/12')
ax.set_xticks(ind + width)
ax.set_xticklabels(('D0', 'D1', 'D2'))

ax.legend((rects1[0], rects2[0]),
          ('Total Num. of Max Hits', 'Total Num. of Min Hits'), loc=3)


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
ax.set_ylim(ymin=60000)

plt.show()
