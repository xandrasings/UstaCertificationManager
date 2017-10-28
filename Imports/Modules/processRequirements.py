from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *
from ..Utilities.xlrdHelper import *

def processRequirements():
	data = selectDataSource('requirements')
	colMax = getColMax(data)
	rowMax = getRowMax(data)
	output(validateFormat(data, colMax, rowMax))


def validateFormat(data, colMax, rowMax):
	output(validateFormat_ranges(colMax, rowMax))
	output(validateFormat_columnHeaders(data, colMax))
	output(validateFormat_rowHeaders(data, rowMax))
	output(validateFormat_data(data, colMax, rowMax))
	return True


def validateFormat_ranges(colMax, rowMax):
	return True


def validateFormat_columnHeaders(data, colMax):
	return True
	


def validateFormat_rowHeaders(data, rowMax):
	return True
	


def validateFormat_data(data, colMax, rowMax):
	return True

