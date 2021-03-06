from ...Utilities.sys import *
from ...Utilities.input import *
from ...Utilities.output import *


def userCheck(result, explanation):
	if not result:
		outputUserNotice(explanation)
		result = promptYN('Proceed anyway?')

	if not result:
		quit()

	return True


def validateRowRange(expectedHeaderRows, rowMax):
	result = rowMax >= expectedHeaderRows
	result = userCheck(result, 'Number of rows (' + str(rowMax) + ') should be above ' + str(expectedHeaderRows))
	return result


def validateColRange(expectedHeaderCols, colMax):
	result = colMax >= expectedHeaderCols
	result = userCheck(result, 'Number of columns (' + str(colMax) + ') should be above ' + str(expectedHeaderCols))
	return result


def validateExpectedLeadingCols(expected, actual, output = True):
	result = True
	index = 0
	indexLimit = len(expected)

	while index < indexLimit:
		if not compareString(expected[index], actual[index]):
			result = False
			break
		index = index + 1

	if not result and output:
		result = outputUserNotice(result, 'Column ' + str(index + 1) + ' is expected to be \'' + expected[index].strip().upper() + '\' but is actually \'' + actual[index] + '\'')
	return result


def validateExpectedLeadingRows(expected, actual):
	result = True
	index = 0
	indexLimit = len(expected)

	while index < indexLimit:
		if not compareString(expected[index], actual[index]):
			result = False
			break
		index = index + 1

	if not result:
		result = userCheck(result, 'Row ' + str(index + 1) + ' is expected to be \'' + expected[index].strip().upper() + '\' but is actually \'' + actual[index] + '\'')
	return result


def compareString(expected, actual):
	return expected.strip().upper() == actual.strip().upper()


def validateHeaderFormat(actual, index):
	result = True
	indexLimit = len(actual)


	while index < indexLimit:
		if not isStringy(actual[index]):
			result = False
			break
		index = index + 1

	if not result:
		result = userCheck(result, 'Header \'' + actual[index] + '\' is expected to be a non-numeric text.')
	return result


def isStringy(text):
	return any(c.isalpha() for c in str(text))


def isBinary(text):
	result = text in [0, 1]
	result = userCheck(result, 'Found non-binary result: ' + str(text) + ' in data.')

	return result

def pare(name, suffixes):
	for suffix in suffixes:
		if name.endswith(suffix.upper()):
			name = pare(name[:-len(suffix)], suffixes)
	return name
			




