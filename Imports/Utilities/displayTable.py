from .color import *
from .logo import *

def displayTable(colHeaders, rowHeaders, data):
	initialColWidth = establishInitialColWidth(rowHeaders)
	print('col width 1:')
	print(initialColWidth)
	colWidth = establishColWidth(initialColWidth, rowHeaders)
	print('col width others:')
	print(colWidth)
	print(data)


def establishInitialColWidth(rowHeaders):
	rowHeaderMax = 0

	for rowHeader in rowHeaders:
		rowHeaderMax = max(rowHeaderMax, 20)

	return rowHeaderMax


def establishColWidth(initialColWidth, colHeaders):
	return ((180 - initialColWidth) // len(colHeaders)) - 1