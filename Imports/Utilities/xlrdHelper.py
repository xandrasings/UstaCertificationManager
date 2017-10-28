def getColMax(data):
	colMax = data.ncols

	for col in range(colMax):
		if(data.cell(0,col).value) == '':
			colMax = col
	return colMax


def getRowMax(data):
	rowMax = data.nrows

	for row in range(rowMax):
		if(data.cell(row,0).value) == '':
			rowMax = row
	return rowMax