import readDataset
from math import sqrt
import matplotlib.pyplot as plt


myRows = readDataset.getRows("Trabalho_1_Datasets/movie_metadata.csv", "facenumber_in_poster", "imdb_score")
# Passando para float pois e mais facil de trabalhar
myRows = [[float(j) for j in i] for i in myRows]

sumRows = [sum(i) for i in zip(*myRows)]
x_mean = sumRows[0]/len(myRows)
y_mean = sumRows[1]/len(myRows)

# Calculando o coeficiente de correlacao de Pearson
a = 0.0
b_x = 0.0
b_y = 0.0
for row in myRows:
	a += ((row[0]-x_mean)*(row[1]-y_mean))
	b_x += (row[0]-x_mean)**2
	b_y += (row[1]-y_mean)**2

b = sqrt(b_x)*sqrt(b_y)
r = a/b
print '''A correlacao entre o numero de faces existentes no poster e \
a nota no imdb e de {: .2f}%'''.format(abs(r)*100)

for i in range(10):
	print myRows[i]

data = [
    ('a', 4),
    ('b', 5),
    ('c', 5),
    ('d', 4),
    ('e', 2),
    ('f', 5),
]
labels, y = zip(*data)

x = range(len(y))
plt.plot(x, y, 'o')
plt.xticks(x, labels)
plt.axis([-1, 8, 0, 6])
#plt.show()




