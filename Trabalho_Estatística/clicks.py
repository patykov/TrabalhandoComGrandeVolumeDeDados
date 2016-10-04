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


X = (( pow((A_yes-E_A_yes), 2)/E_A_yes) + (pow((A_no-E_A_no), 2)/E_A_no) + 
	(pow((B_yes-E_B_yes), 2)/E_B_yes) + (pow((B_no-E_B_no), 2)/E_B_no))

# Para k = 4 com alpha = 0.05, temos Xc = 3.841 
Xc = 3.841
if X < Xc: print 'Pertencem a mesma populacao pois encontra-se dentro do intervalo definido: {: .3f} < {: .3f}!!'.format(X,Xc)
else: print 'Nao pertencem a mesma populacao pois ultrapassa o intervalo definido: {: .3f} >= {: .3f}'.format(X,Xc)

# plot the distributions
fig, ax = plt.subplots(figsize=(12, 6))
fig.subplots_adjust(bottom=0.12)
x = np.linspace(-1, 20, 1000)

dist = chi2(4, 0)

plt.plot(x, dist.pdf(x), c='black', label=r'$k=4$')
plt.axvline(x=Xc, ymin=0, ymax = dist.pdf(Xc), linewidth=2, color='r')
plt.axvline(x=X, ymin=0, ymax = dist.pdf(X), linewidth=2, color='b')

plt.xlim(0, 15)
plt.ylim(0, 0.3)

plt.xlabel('$Q$')
plt.ylabel(r'$p(Q|k)$')
plt.title(r'$\chi^2\ \mathrm{Distribution}$')

plt.legend()
plt.show()





