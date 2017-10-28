from .selectDataSource import *
from ..Objects.Data import *
from ..Utilities.input import *
from ..Utilities.output import *

#todo warn user if lines will be ignored

def processRequirements():
	data = selectDataSource('requirements')
	data.pareColMax()
	data.pareRowMax()
	data.validate()


def validateFormat(data):
	output(validateFormat_ranges(data))
	output(validateFormat_columnHeaders(data))
	output(validateFormat_rowHeaders(data))
	output(validateFormat_data(data))
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

