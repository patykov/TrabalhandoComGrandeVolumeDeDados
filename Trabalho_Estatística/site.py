import csv
import os
import matplotlib.pyplot as plt
from math import sqrt

sumPopTime = 0.0
dpPop = 0.0
totPop = 0
sumAmsTime = 0.0
dpAms = 0.0
totAms = 0

# Calculando a media da populacao
with open("Trabalho_1_Datasets/populacao_tempo.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		sumPopTime += float(row.split(";")[1])
		totPop += 1

	popMean = sumPopTime/totPop

# Calculando o desvio padrao da populacao
with open("Trabalho_1_Datasets/populacao_tempo.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		dpPop += pow((float(row.split(";")[1]) - popMean), 2)

	dpPop = sqrt(dpPop/(totPop-1))

# Lendo a media da amostra
with open("Trabalho_1_Datasets/amostra_tempo.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		sumAmsTime += float(row.split(";")[1])
		totAms += 1

	amsMean = sumAmsTime/totAms

# Calculando o desvio padrao da amostra
with open("Trabalho_1_Datasets/amostra_tempo.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		dpAms += pow((float(row.split(";")[1]) - amsMean), 2)

	dpAms = sqrt(dpAms/(totAms-1))


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



