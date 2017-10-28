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


	def validate(self):
		return self.validateRanges() and self.validateColHeaders() and self.validateRowHeaders() and self.validateData()



	def validateRanges(self):
		result = True
		if doValidateDateRanges[self.dataType]:
			output('validateRanges against ' + self.dataType)

		return result


	def validateColHeaders(self):
		result = True
		if doValidateColHeaders[self.dataType]:
			output('validateColHeaders against ' + self.dataType)

		return result


	def validateRowHeaders(self):
		result = True
		if doValidateRowHeaders[self.dataType]:
			output('validateRowHeaders against ' + self.dataType)

		return result


	def validateData(self):
		result = True
		if doValidateData[self.dataType]:
			output('validateData against ' + self.dataType)

		return result
