from .selectDataSource import *
from ..Objects.Data import *
from ..Utilities.input import *
from ..Utilities.output import *
from ..Utilities.xlrdHelper import *

#todo warn user if lines will be ignored

def processRequirements():
	data = selectDataSource('requirements')
	print(data.getArea())
	# colMax = getColMax(data)
	# rowMax = getRowMax(data)
	# output(validateFormat(data, colMax, rowMax))


def validateFormat(data, colMax, rowMax):
	output(validateFormat_ranges(colMax, rowMax))
	output(validateFormat_columnHeaders(data, colMax))
	output(validateFormat_rowHeaders(data, rowMax))
	output(validateFormat_data(data, colMax, rowMax))
	return True


def validateFormat_ranges(colMax, rowMax):
	return colMax > 1 and rowMax > 1


def validateFormat_columnHeaders(data, colMax):
	# if data.cell(0,0).value.strip().upper() != 'DISCIPLINE':
	# 	return False
	# for col in range(1, colMax):
	# 	try:
	# 		float(data.cell(0,0).value.strip())
	# 		return False
	# 	except:
	# 		continue
	return True
	

def validateFormat_rowHeaders(data, rowMax):
	return True
	


def validateFormat_data(data, colMax, rowMax):
	return True

