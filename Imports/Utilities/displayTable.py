from .output import *

def displayTable(colHeaders, rowHeaders, data):
	initialColWidth = establishInitialColWidth(rowHeaders)
	colWidth = establishColWidth(initialColWidth, colHeaders)
	colHeaders = addPrecedingCell(colHeaders)

	displayRow(initialColWidth, colWidth, colHeaders)
	# displayRows!


def establishInitialColWidth(rowHeaders):
	rowHeaderMax = 0

	for rowHeader in rowHeaders:
		rowHeaderMax = max(rowHeaderMax, 20)

	return rowHeaderMax


def establishColWidth(initialColWidth, colHeaders):
	return ((180 - initialColWidth) // len(colHeaders)) - 1


def addPrecedingCell(colHeaders):
	# TODO change me
	# colHeaders = [''].extend(colHeaders)

	fullColHeaders = ['']
	fullColHeaders.extend(colHeaders)

	return fullColHeaders


def displayRow(initialColWidth, colWidth, rowContent): # array of strings
	rowContent = formatRowContents(initialColWidth, colWidth, rowContent) # array of arrays

	outputRow(rowContent)
	outputLine()


def formatRowContents(initialColWidth, colWidth, rowContent): # array of strings
	rowContent = arrayenRowContent(initialColWidth, colWidth, rowContent) # array of array of strings
	rowContent = lengthenRowContent(rowContent)
	rowContent = buffenRowContent(initialColWidth, colWidth, rowContent)
	rowContent = stringenRowContent(rowContent)

	return rowContent


def arrayenRowContent(initialColWidth, colWidth, rowContent): # array of strings
	rowContentArray = [] # array 

	chosenWidth = initialColWidth
	for cellContent in rowContent:
		rowContentArray.append(arrayenCellContent(chosenWidth, cellContent))
		chosenWidth = colWidth

	return rowContentArray # array of array of strings


def arrayenCellContent(colWidth, cellContent): #string
	cellContent = cellContent.split() #array of strings
	return cellContent #array of strings


def lengthenRowContent(rowContent): # array of array of strings
	cellDepth = getCellDepth(rowContent)

	rowContentArray = [] # array 

	for cellContent in rowContent: # array of strings
		rowContentArray.append(lengthenCellContent(cellDepth, cellContent))

	return rowContentArray # array of array of strings


def getCellDepth(rowContent): # array of array of strings
	cellDepth = 0
	for cellContent in rowContent:
		cellDepth = max(cellDepth, len(cellContent))
	return cellDepth


def lengthenCellContent(cellDepth, cellContent): # array of strings
	buffer = cellDepth - len(cellContent)
	for i in range(buffer):
		cellContent.append('')
	return cellContent


def buffenRowContent(initialColWidth, colWidth, rowContent): # array of array of strings
	rowContentArray = [] # array 

	chosenWidth = initialColWidth
	for cellContent in rowContent:
		rowContentArray.append(buffenCellContent(chosenWidth, cellContent))
		chosenWidth = colWidth

	return rowContentArray # array of array of strings


def buffenCellContent(colWidth, cellContent): # array of strings
	newCellContent = []

	for cellRow in cellContent: # string
		newCellContent.append(buffenCellRow(colWidth, cellRow))

	return newCellContent # array of strings


def buffenCellRow(colWidth, cellRow): # string
	buffer = colWidth - len(cellRow)
	frontBuffer = buffer // 2
	backBuffer = buffer - frontBuffer
	return generateBuff(frontBuffer) + cellRow + generateBuff(frontBuffer)


def generateBuff(buffer):
	buff = ''

	for i in range(buffer):
		buff = buff + ' '

	return buff


def stringenRowContent(rowContent): # array of array of strings
	rowContentArray = [] # array 

	for i in range(getCellDepth(rowContent)):
		subRow = ''
		for cellContent in rowContent:
			subRow = subRow + cellContent[i] + '|'
		rowContentArray.append(subRow)

	return rowContentArray # array of strings


def outputRow(rowContent): # array of strings
	for subRow in rowContent:
		output(subRow)



