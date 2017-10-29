from .color import *
from .logo import *

def displayTable(colHeaders, rowHeaders, data):
	colWidth = establishColWidth(colHeaders, rowHeaders)


def establishColWidth(colHeaders, rowHeaders):
	rowHeaderMax = establishRowHeaderMax(rowHeaders)


def establishRowHeaderMax(rowHeaders):
	rowHeaderMax = 0

	for rowHeader in rowHeaders:
		rowHeaderMax = max(rowHeaderMax, len(rowHeader))

	rowHeaderMax = min(rowHeaderMax, 20)	