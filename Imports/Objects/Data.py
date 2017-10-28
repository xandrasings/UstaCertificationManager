from .Helpers.DataHelper import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Data:
	def __init__(self, data, dataType):
		self.data = data
		self.dataType = dataType
		self.colMax = self.data.ncols
		self.rowMax = self.data.nrows


	def setUp(self):
		if doPareColMax[self.dataType]:
			self.pareColMax()
		if doPareRowMax[self.dataType]:
			self.pareRowMax()
		self.validate()


	def get(self, row, col):
		val = self.data.cell(row, col).value
		if type(val) is str:
			val = val.strip().upper()
		return val


	def getColMax(self):
		return self.colMax


	def getRowMax(self):
		return self.rowMax


	def pareColMax(self):
		colMax = self.colMax

		for col in range(colMax):
			if(self.get(0,col)) == '':
				colMax = col
				outputUserNotice('Last column considered will be ' + self.get(0,colMax-1))
				break
		self.colMax = colMax


	def pareRowMax(self):
		rowMax = self.rowMax

		for row in range(rowMax):
			if(self.get(row,0)) == '':
				rowMax = row
				outputUserNotice('Last row considered will be ' + self.get(rowMax-1,0))
				break
		self.rowMax = rowMax


	def getFullColHeaders(self):
		colHeaders = []

		for col in range(self.colMax):
			colHeaders.append(self.get(0,col))

		return colHeaders


	def getMainColHeaders(self):
		colHeaders = []

		for col in range(len(expectedLeadingCols[self.dataType]), self.colMax):
			colHeaders.append(self.get(0,col))

		return colHeaders


	def getFullRowHeaders(self):
		rowHeaders = []

		for row in range(self.rowMax):
			rowHeaders.append(self.get(row,0))

		return rowHeaders


	# def getMainRowHeaders(self):
	# 	rowHeaders = []

	# 	for row in range(len(expectedLeadingRows[self.dataType]), self.rowMax):
	# 		rowHeaders.append(self.get(row,0))

	# 	return rowHeaders


	def validate(self):
		return (
			self.validateRanges() and
			self.validateColHeaders() and
			self.validateRowHeaders() and
			self.validateData()
		)


	def validateRanges(self):
		result = True
		if doValidateRanges[self.dataType]:
			result = (
				validateRowRange(expectedHeaderRows[self.dataType], self.rowMax) and
				validateColRange(expectedHeaderCols[self.dataType], self.colMax)
			)

		return result


	def validateColHeaders(self):
		result = True
		if doValidateColHeaders[self.dataType]:
			expected = expectedLeadingCols[self.dataType]
			actual = self.getFullColHeaders()
			result = (
				validateExpectedLeadingCols(expected, actual) if doValidateExpectedLeadingCols[self.dataType] else True and
				validateHeaderFormat(actual, len(expected)) if doValidateColHeaderFormat[self.dataType] else True
			)

		return result


	def validateRowHeaders(self):
		result = True
		if doValidateRowHeaders[self.dataType]:
			expected = expectedLeadingRows[self.dataType]
			actual = self.getFullRowHeaders()
			result = (
				validateExpectedLeadingRows(expected, actual) if doValidateExpectedLeadingRows[self.dataType] else True and
				validateHeaderFormat(actual, len(expected)) if doValidateRowHeaderFormat[self.dataType] else True
			)

		return result


	def validateData(self):
		result = True
		if doValidateData[self.dataType]:
			# TODO options other than Binary
			result = self.validateBinaryData()

		return result


	def validateBinaryData(self):
		result = True
		rowStart = len(expectedLeadingRows[self.dataType])
		rowMax = self.rowMax
		colStart = len(expectedLeadingCols[self.dataType])
		colMax = self.colMax

		rowIndex = rowStart
		colIndex = colStart

		while rowIndex < rowMax:
			while colIndex < colMax:
				if not isBinary(self.get(rowIndex, colIndex)):
					result = False
					break
				colIndex = colIndex + 1
			if not result:
				break
			rowIndex = rowIndex + 1
			colIndex = colStart

		return result


	def convertCols(self, givenArgs = []):
		colObjects = []

		startCol = len(expectedLeadingCols[self.dataType])

		for col in range(startCol, self.colMax):
			dataArgs = []
			for dataArgIndex in range(startCol):
				dataArgs.append(self.get(dataArgIndex,col))
				
			colObjects.append(colHeaderType[self.dataType](dataArgs, givenArgs))

		return colObjects


	def convertRows(self, givenArgs = []):
		rowObjects = []

		startRow = len(expectedLeadingRows[self.dataType])

		for row in range(startRow, self.rowMax):
			dataArgs = []
			for dataArgIndex in range(self.colMax):
				dataArgs.append(self.get(row,dataArgIndex))
				
			rowObjects.append(rowHeaderType[self.dataType](dataArgs, givenArgs))

		return rowObjects
