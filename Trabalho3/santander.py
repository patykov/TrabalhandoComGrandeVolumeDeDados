import numpy as np 

myRows = []
with open("dataset_trabalho3/train_file.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		cells = row[:-1].split(',')
		cells = map(float, cells)
		myRows.append(cells)
myRows = np.array(myRows)

equalCol = []
normalizeByMean = []
normalizeByMedian = []
for i in range((myRows.shape)[1]):
	myCol = myRows[:, i]
	mean = np.mean(myCol)
	median = np.median(myCol)
	dp = np.std(myCol)
	if dp == 0:
		equalCol.append(i)
	else: 
		print '{} -> Mean: {}, Median: {}, Dp: {} \n'.format(i, mean, median, dp)

for col in equalCol[::-1]:
	myRows = np.delete(myRows, col, 1)

