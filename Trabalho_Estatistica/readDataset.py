def getRows(fileName, x, y):
	myRows = []

	with open(fileName) as csvFile:
		header = csvFile.readline().split(",")
		rowSize = len(header)
		x_id = [i for i, v in enumerate(header) if v in x][0]
		y_id = [i for i, v in enumerate(header) if v in y][0]
		for row in csvFile:
			cells = row.split(",")
			numCells = len(cells)
			# Consideramos apenas as linhas que seguem o padrao esperado
			if numCells == rowSize:
				# Das linhas 'ok', precisamos que os valores nao sejam vazios
				myRow = [cells[x_id], cells[y_id]]
				if not any(v is '' for v in myRow):
					myRows.append(myRow)

	return myRows