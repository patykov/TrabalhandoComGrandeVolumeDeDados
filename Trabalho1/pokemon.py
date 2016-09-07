import csv
import os
import matplotlib.pyplot as plt

# Creating the Dict where I will save the sum of each atribute
legendaries = {'HP': 0, 'Attack': 0, 'Defense': 0, 'Sp. Atk': 0, 'Sp. Def': 0, 'Speed': 0}
numLegendary = 0
normals = []
upTheLevel = {'1': 0, '2': 0, '3': 0, '4':0, '5': 0, '6': 0}

# Reading the file and getting the sum of the attributes values
with open("Pokemon.csv") as csvFile:
	reader = csv.DictReader(csvFile)
	for row in reader:
		if (row["Legendary"] == "True"):
			legendaries = {k: legendaries.get(k, 0) + int(row.get(k, 0)) for k in set(legendaries)}
			numLegendary = numLegendary+1
		else:
			normals.append(row)

# Calculate the mean of each attribute
legendaries.update((x, y/numLegendary) for x, y in legendaries.items())

# Find the normal pokemons which have at least X attributes better than the legendary's mean
for poke in normals:
	better = 0
	for attr in set(legendaries):
		if int(poke[attr]) > int(legendaries[attr]):
			better += 1
	if better:
		for i in range(better):
			upTheLevel[str(i+1)] += 1

# Get the % of pokemons for each situation
upTheLevel = {k: (upTheLevel.get(k, 0)*1.0/len(normals)*1.0)*100 for k in set(upTheLevel)}

# Print the results
print 'Percentage of normal pokemons with at least: \n'
for k in upTheLevel:
	print  str(k) + ' attributes above the legendary\'s level: ' + str(upTheLevel[k]) + '\n'

