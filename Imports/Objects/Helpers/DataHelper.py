from ...Modules.quit import *
from ...Utilities.output import *
from ...Utilities.output import *

def userCheck(result, explanation):
	if not result:
		outputUserNotice(explanation)
		result = promptYN('Proceed anyway?')

	if not result:
		quit()

	return True


def validateRowRange(expectedHeaderRows, rowMax):
	result = rowMax > expectedHeaderRows
	result = userCheck(result, 'Number of rows (' + str(rowMax) + ') should be above ' + str(expectedHeaderRows))
	return result


def validateColRange(expectedHeaderCols, colMax):
	result = colMax > expectedHeaderCols
	result = userCheck(result, 'Number of columns (' + str(colMax) + ') should be above ' + str(expectedHeaderCols))
	return result