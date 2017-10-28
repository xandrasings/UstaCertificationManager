from .Helpers.DataHelper import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Data:
	def __init__(self, data, dataType):
		self.data = data
		self.dataType = dataType
		self.colMax = self.data.ncols
		self.rowMax = self.data.nrows


	def startUp(self):
		if doPareColMax[self.dataType]:
			self.pareColMax()
		if doPareRowMax[self.dataType]:
			self.pareRowMax()
		self.validate()


	def get(self, row, col):
		return self.data.cell(row, col).value.strip().upper()


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


	def getColHeaders(self):
		colHeaders = []

		for col in range(self.colMax):
			colHeaders.append(self.get(0,col))

		return colHeaders


	def getRowHeaders(self):
		rowHeaders = []

		for row in range(self.rowMax):
			rowHeaders.append(self.get(row,0))

		return rowHeaders


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
			actual = self.getColHeaders()
			result = (
				validateExpectedLeadingCols(expected, actual) if doValidateExpectedLeadingCols[self.dataType] else True and
				validateHeaderFormat(actual, len(expected)) if doValidateColHeaderFormat[self.dataType] else True
			)

		return result


	def validateRowHeaders(self):
		result = True
		if doValidateRowHeaders[self.dataType]:
			expected = expectedLeadingRows[self.dataType]
			actual = self.getRowHeaders()
			result = (
				validateExpectedLeadingRows(expected, actual) if doValidateExpectedLeadingRows[self.dataType] else True and
				validateHeaderFormat(actual, len(expected)) if doValidateRowHeaderFormat[self.dataType] else True
			)

		return result


	def validateData(self):
		result = True
		if doValidateData[self.dataType]:
			output('validateData against ' + self.dataType)

		return result
