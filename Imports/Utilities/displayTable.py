from .output import *
from .color import *

def displayTable(colHeaders, rowHeaders, data, tableCode = []):
	colorCode = {tableCodeDetail[0]: tableCodeDetail[2] for tableCodeDetail in tableCode}
	initialColWidth = establishInitialColWidth(rowHeaders)
	colWidth = establishColWidth(initialColWidth, colHeaders)

	displayTableKey(tableCode)
	displayRow(initialColWidth, colWidth, colHeaders)
	displayRows(initialColWidth, colWidth, data, rowHeaders, colorCode)
	displayTableKey(tableCode)


def establishInitialColWidth(rowHeaders):
	rowHeaderMax = 0

	for rowHeader in rowHeaders:
		rowHeaderMax = max(rowHeaderMax, 20)

	return rowHeaderMax


def establishColWidth(initialColWidth, colHeaders):
	return ((getTerminalWidth() - initialColWidth) // len(colHeaders)) - 1


def displayTableKey(tableCode):
	if len(tableCode) > 0:
		adjustment = max(getCellDepth(tableCode), 4)
		outputBlank()
		output('CODE'.ljust(adjustment) + ' MEANING')
		for tableCodeDetail in tableCode:
			output(color(tableCodeDetail[0].ljust(adjustment), tableCodeDetail[2]) + ' ' + tableCodeDetail[1])
		outputBlank()


def displayRows(initialColWidth, colWidth, rowsContent, rowHeaders, colorCode):
	for i in range(min(len(rowsContent), len(rowHeaders))):
		displayRow(initialColWidth, colWidth, rowsContent[i], rowHeaders[i], colorCode)


def displayRow(initialColWidth, colWidth, rowContent, firstRowContent = '', colorCode = {}):
	rowContent = combineRowContent(rowContent, firstRowContent)
	rowContent = formatRowContents(initialColWidth, colWidth, rowContent, colorCode)

	outputRow(rowContent)
	outputLine()


def combineRowContent(rowContent, firstRowContent):
	fullRowContent = [firstRowContent]
	fullRowContent.extend(rowContent)

	return fullRowContent


def formatRowContents(initialColWidth, colWidth, rowContent, colorCode):
	rowContent = applycolorCode(rowContent, colorCode)
	rowContent = arrayenRowContent(initialColWidth, colWidth, rowContent)
	rowContent = lengthenRowContent(rowContent)
	rowContent = buffenRowContent(initialColWidth, colWidth, rowContent)
	rowContent = stringenRowContent(rowContent)

	return rowContent


def applycolorCode(rowContent, colorCode):
	rowContentRevised = []

	for cellContent in rowContent:
		rowContentRevised.append([cellContent, (colorCode[cellContent] if cellContent in colorCode else 'black')])

	return rowContentRevised


def arrayenRowContent(initialColWidth, colWidth, rowContent):
	rowContentArray = []

	chosenWidth = initialColWidth
	for cellContent in rowContent:
		rowContentArray.append([arrayenCellContent(chosenWidth, cellContent[0]), cellContent[1]])
		chosenWidth = colWidth

	return rowContentArray


def arrayenCellContent(colWidth, cellContent):
	arrayenedCellContent = []
	wordArray = cellContent.split()

	row = ''
	while(len(wordArray) > 0):
		rowEmpty = checkIfRowIsEmpty(row)
		if fits(row, colWidth, wordArray[0], rowEmpty):
			row = row + ('' if rowEmpty else ' ') + wordArray[0]
			wordArray.pop(0)
		else:
			if rowEmpty:
				row = getWordPrefix(wordArray[0], colWidth)
				wordArray[0] = getWordSuffix(wordArray[0], colWidth)
			arrayenedCellContent.append(row)
			row = ''

	if len(row) > 0:
		arrayenedCellContent.append(row)

	return arrayenedCellContent


def fits(row, max, word, emptyRow):
	return len(row) + len(word) + (0 if emptyRow else 1) <= max


def checkIfRowIsEmpty(row):
	return len(row) == 0


def getWordPrefix(word, colWidth):
	return word[0:colWidth-1] + '-'


def getWordSuffix(word, colWidth):
	return word[colWidth-1:]


def lengthenRowContent(rowContent):
	cellDepth = getCellDepth(rowContent)

	rowContentArray = []

	for cellContent in rowContent:
		rowContentArray.append([lengthenCellContent(cellDepth, cellContent[0]),cellContent[1]])

	return rowContentArray


def getCellDepth(rowContent):
	cellDepth = 0
	for cellContent in rowContent:
		cellDepth = max(cellDepth, len(cellContent[0]))
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
		rowContentArray.append([buffenCellContent(chosenWidth, cellContent[0]), cellContent[1]])
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
			subRow = subRow + color(cellContent[0][i], cellContent[1]) + '|'
		rowContentArray.append(subRow)

	return rowContentArray


def outputRow(rowContent):
	for subRow in rowContent:
		output(subRow)



