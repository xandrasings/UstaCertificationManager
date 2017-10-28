from ..Utilities.output import *

class Data:
	def __init__(self, data, dataType):
		self.data = data
		self.dataType = dataType
		self.colMax = self.data.ncols
		self.rowMax = self.data.nrows


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
		output('validating against ' + self.dataType)


	def validateRanges(self):
		output('validating against ' + self.dataType)


	def validateColHeaders(self):
		output('validating against ' + self.dataType)


	def validateRowHeaders(self):
		output('validating against ' + self.dataType)


	def validateData(self):
		output('validating against ' + self.dataType)
