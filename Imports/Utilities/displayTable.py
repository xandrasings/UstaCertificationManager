from .output import *
from .color import *

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
	return ((getTerminalWidth() - initialColWidth) // len(colHeaders)) - 1


def combineRowContent(rowContent, firstRowContent):
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

	return rowContentArray


def arrayenCellContent(colWidth, cellContent):
	arrayenedCellContent = []
	wordArray = cellContent.split()

	row = ''
	while(len(wordArray) > 0):
		if fits(row, colWidth, wordArray[0]):
			row = row + ' ' + wordArray[0]
			wordArray.pop(0)
		else:
			if rowIsEmpty(row):
				row = getWordPrefix(wordArray[0], colWidth)
				wordArray[0] = getWordSuffix(wordArray[0], colWidth)
			arrayenedCellContent.append(row)
			row = ''

	if len(row) > 0:
		arrayenedCellContent.append(row)

	return arrayenedCellContent


def fits(row, max, word):
	return len(row) + len(word) + (0 if rowIsEmpty(row) else 1) <= max


def rowIsEmpty(row):
	return len(row) == 0


def getWordPrefix(word, colWidth):
	return word[0:colWidth-1] + '-'


def getWordSuffix(word, colWidth):
	return word[colWidth-1:]


def lengthenRowContent(rowContent):
	cellDepth = getCellDepth(rowContent)

	rowContentArray = []

	for cellContent in rowContent:
		rowContentArray.append(lengthenCellContent(cellDepth, cellContent))

	return rowContentArray


def getCellDepth(rowContent):
	cellDepth = 0
	for cellContent in rowContent:
		cellDepth = max(cellDepth, len(cellContent))
	return cellDepth


def lengthenCellContent(cellDepth, cellContent):
	fullBuffer = cellDepth - len(cellContent)
	for i in range(fullBuffer):
		cellContent.append('')
	return cellContent


def buffenRowContent(initialColWidth, colWidth, rowContent):
	rowContentArray = []

	chosenWidth = initialColWidth
	for cellContent in rowContent:
		rowContentArray.append(buffenCellContent(chosenWidth, cellContent))
		chosenWidth = colWidth

	return rowContentArray


def buffenCellContent(colWidth, cellContent):
	newCellContent = []

	for cellRow in cellContent:
		newCellContent.append(buffenCellRow(colWidth, cellRow))

	return newCellContent


def buffenCellRow(colWidth, cellRow):
	fullBuffer = colWidth - len(cellRow)
	frontBuffer = fullBuffer // 2
	backBuffer = fullBuffer - frontBuffer
	return generateBuff(frontBuffer) + cellRow + generateBuff(backBuffer)


def generateBuff(fullBuffer):
	buff = ''

	for i in range(fullBuffer):
		buff = buff + ' '

	return buff


def stringenRowContent(rowContent):
	rowContentArray = []

	for i in range(getCellDepth(rowContent)):
		subRow = ''
		for cellContent in rowContent:
			subRow = subRow + cellContent[i] + '|'
		rowContentArray.append(subRow)

	return rowContentArray


def outputRow(rowContent):
	for subRow in rowContent:
		output(subRow)



