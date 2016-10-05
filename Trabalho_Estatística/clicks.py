from math import sqrt
import numpy as np
from scipy.stats import chi2
from matplotlib import pyplot as plt

"""
Tabela Observada          Tabela Esperada
        A       B                A          B
yes | A_yes | B_yes |     yes | E_A_yes | E_B_yes |
no  | A_no  | B_no  |     no  | E_A_no  | E_B_no  |

"""

A_yes = 0.0
A_no = 0.0
B_yes = 0.0
B_no = 0.0

# Calculando as classes para a amostra A
with open("Trabalho_1_Datasets/amostra_A_click.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		if "yes" in row.split(";")[1]: A_yes += 1
		else: A_no += 1

# Calculando as classes para a amostra B
with open("Trabalho_1_Datasets/amostra_B_click.csv") as csvFile:
	csvFile.readline() #Retirando a primeira linha
	for row in csvFile:
		if "yes" in row.split(";")[1]: B_yes += 1
		else: B_no += 1

T = A_yes + A_no + B_yes + B_no

E_A_yes = ((A_yes+B_yes)*(A_no+A_yes))/T
E_A_no = ((A_no+B_no)*(A_no+A_yes))/T
E_B_yes = ((A_yes+B_yes)*(B_yes+B_no))/T
E_B_no = ((B_no+B_yes)*(A_no+B_no) )/T

print 'A yes = {: .5f}  B yes = {: .5f} \n A no = {: .5f} B no = {: .5f}'.format(A_yes,B_yes,A_no,B_no)
print 'Valores esperados:\n'
print 'A yes = {: .5f}  B yes = {: .5f} \n A no = {: .5f} B no = {: .5f}'.format(E_A_yes,E_B_yes,E_A_no,E_B_no)



X = (( pow((A_yes-E_A_yes), 2)/E_A_yes) + (pow((A_no-E_A_no), 2)/E_A_no) + 
	(pow((B_yes-E_B_yes), 2)/E_B_yes) + (pow((B_no-E_B_no), 2)/E_B_no))

# Para k = 4 com alpha = 0.05, temos Xc = 3.841 
Xc = 3.841
if X < Xc: print 'Pertencem a mesma populacao pois encontra-se dentro do intervalo definido: {: .3f} < {: .3f}!!'.format(X,Xc)
else: print 'Nao pertencem a mesma populacao pois ultrapassa o intervalo definido: {: .3f} >= {: .3f}'.format(X,Xc)

################################################################################################################################



Yes = (A_yes, B_yes)
No = (A_no, B_no)

fig, ax = plt.subplots()

index = np.arange(2)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, Yes, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Yes')

rects2 = plt.bar(index + bar_width, No, bar_width,
                 alpha=opacity,
                 color='r',
                 label='No')

plt.xlabel('Amostras')
plt.ylabel('Clicks')
plt.xticks(index + bar_width, ('A', 'B'))
plt.legend()

#plt.tight_layout()
plt.show()





