from .output import *

def displayTable(colHeaders, rowHeaders, data):
	initialColWidth = establishInitialColWidth(rowHeaders)
	colWidth = establishColWidth(initialColWidth, colHeaders)

	displayHeader(initialColWidth, colWidth, colHeaders)


def establishInitialColWidth(rowHeaders):
	rowHeaderMax = 0

	for rowHeader in rowHeaders:
		rowHeaderMax = max(rowHeaderMax, 20)

	return rowHeaderMax


def establishColWidth(initialColWidth, colHeaders):
	return ((180 - initialColWidth) // len(colHeaders)) - 1


def displayHeader(initialColWidth, colWidth, colHeaders):
	initialColumnHeader = getBlankInitialColumnHeader(initialColWidth)
	columnContent = getColumnContent(colWidth, colHeaders)

	displayRow(columnContent, initialColumnHeader)
	outputLineHeavy()


def getBlankInitialColumnHeader(initialColWidth):
	result = ''
	for i in range(initialColWidth):
		result = result + '-'

	return result


def getColumnContent(colWidth, colHeaders):
	result = ''
	for colHeader in colHeaders:
		result = result + getColumnHeader(colWidth, colHeader)

	return result


def getColumnHeader(colWidth, colHeader):
	if len(colHeader) > colWidth:
		colHeader = colHeader[0:colWidth]

	buffer = getBuffer(colWidth, colHeader)
	print(buffer)
	colHeader = '|' + colHeader + buffen(buffer)
	return colHeader


def getBuffer(colWidth, colHeader):
	return colWidth - len(colHeader)


def buffen(buffer):
	result = ''
	for i in range(buffer):
		result = result + ' '

	return result


def displayRow(columnContent, initialColumn = ''):
	output(initialColumn + columnContent)
	outputLine()