import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from math import sqrt


popValues = []
amsValues = []

# Lendo dados da populacao
with open("Trabalho_1_Datasets/populacao_tempo.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		time = float(row.split(";")[1])
		popValues.append(time)

popMean = sum(popValues)/len(popValues)
dpPop = [pow((i - popMean), 2) for i in popValues]
dpPop = sqrt(sum(dpPop)/len(popValues))


# Lendo dados da amostra
with open("Trabalho_1_Datasets/amostra_tempo.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		time = float(row.split(";")[1])
		amsValues.append(time)

amsMean = sum(amsValues)/len(amsValues)
dpAms = [pow((i - amsMean), 2) for i in amsValues]
dpAms = sqrt(sum(dpAms)/len(amsValues))


#Teste da Hipotese usando alpha = 0.05
z = (amsMean - popMean)/(dpPop - sqrt(dpAms))
if (z > 1.96):
	# Nao faz parte da distribuicao normal da populacao - Hipotese rejeitada
	custo = 0.005*len(amsValues)
	lucro = 0.05*(amsMean - popMean)

	if(lucro>custo):
		print 'A nova feature deve ser mantida pois gera {: .5f} centavos de lucro!'.format(lucro-custo)
	else:
		print 'A nova feature nao deve ser mantida pois gera {: .5f} centavos de prejuizo'.format(custo-lucro)

else:
	print "A amostra nao apresentou mudancas significativas em relacao aos dados da populacao"


###########################################################################################################
print 'Media da populacao = {: .5f}'.format(popMean)
print 'Media da amostra = {: .5f}'.format(amsMean)

###########################################################################################################
# Plotando os graficos

# h = sorted(popValues)  

# fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
# plt.plot(h,fit)
#plt.show() 

















