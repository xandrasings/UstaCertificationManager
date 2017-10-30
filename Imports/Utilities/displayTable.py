from .output import *

def displayTable(colHeaders, rowHeaders, data):
	initialColWidth = establishInitialColWidth(rowHeaders)
	colWidth = establishColWidth(initialColWidth, colHeaders)

	displayRow(initialColWidth, colWidth, colHeaders)
	displayRows(initialColWidth, colWidth, data, rowHeaders)


def establishInitialColWidth(rowHeaders):
	rowHeaderMax = 0

	for rowHeader in rowHeaders:
		rowHeaderMax = max(rowHeaderMax, 20)

	return rowHeaderMax


def establishColWidth(initialColWidth, colHeaders):
	return ((180 - initialColWidth) // len(colHeaders)) - 1


def combineRowContent(rowContent, firstRowContent):
	# TODO change me
	# colHeaders = [''].extend(colHeaders)

	fullRowContent = [firstRowContent]
	fullRowContent.extend(rowContent)

	return fullRowContent


def displayRows(initialColWidth, colWidth, rowsContent, rowHeaders):
	for i in range(min(len(rowsContent), len(rowHeaders))):
		displayRow(initialColWidth, colWidth, rowsContent[i], rowHeaders[i])


def displayRow(initialColWidth, colWidth, rowContent, firstRowContent = ''): # array of strings
	rowContent = combineRowContent(rowContent, firstRowContent)
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
	arrayenedCellContent = []
	wordArray = cellContent.split() #array of strings

	row = ''
	for word in wordArray:
		if fits(row, colWidth, word):
			row = (word if rowIsEmpty(row) else row + ' ' + word)
		else:
			arrayenedCellContent.append(row)
			row = word
	arrayenedCellContent.append(row)

	return arrayenedCellContent #array of strings

def fits(row, max, word):
	return len(row) + len(word) + (0 if rowIsEmpty(row) else 1) <= max

def rowIsEmpty(row):
	return len(row) == 0


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
	fullBuffer = cellDepth - len(cellContent)
	for i in range(fullBuffer):
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
	fullBuffer = colWidth - len(cellRow)
	frontBuffer = fullBuffer // 2
	backBuffer = fullBuffer - frontBuffer
	return generateBuff(frontBuffer) + cellRow + generateBuff(backBuffer)


def generateBuff(fullBuffer):
	buff = ''

	for i in range(fullBuffer):
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



