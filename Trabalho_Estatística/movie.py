import readDataset
from math import sqrt
import matplotlib.pyplot as plt


myRows = readDataset.getRows("Trabalho_1_Datasets/movie_metadata.csv", "facenumber_in_poster", "imdb_score")
myRows = [[float(j) for j in i] for i in myRows]
sumRows = [sum(i) for i in zip(*myRows)]
print sumRows
print len(myRows)
x_mean = sumRows[0]/len(myRows)
y_mean = sumRows[1]/len(myRows)
print x_mean
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
print r


labels, y = zip(*myRows)

# x = range(len(y))
# plt.plot(x, y, 'o')
# plt.xticks(x, labels)
# plt.axis([-1, 6, 0, 6])
# plt.show()


#print "Media de clicks em A: " + str(A_Mean) + " \n"
#print "Desvio padrao da populacao: " + str(dpPop) + " \n"
#print "Media de clicks em B: " + str(B_Mean) + " \n"
#print "Desvio padrao da amostra: " + str(dpAms) + " \n"

"""
#Teste da Hipotese usando alpha = 0.05
z = (amsMean - popMean)/(dpPop - sqrt(dpAms))
if (z > 1.96):
	# Nao faz parte da distribuicao normal da populacao - Hipotese rejeitada
	custo = 0.005*totAms
	lucro = 5*(amsMean - popMean)

	if(lucro>custo):
		print 'A nova feature deve ser mantida pois gera {} centavos de lucro!'.format(lucro-custo)
	else:
		print 'A nova feature nao deve ser mantida pois gera {} centavos de prejuizo'.format(custo-lucro)

else:
	print "A amostra nao apresentou mudancas significativas em relacao aos dados da populacao"

"""

