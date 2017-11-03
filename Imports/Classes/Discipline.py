from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Discipline:
	def __init__(self, sourceFile, dataArgs, givenArgs = []):
		self.valid = True
		self.name = dataArgs[0]
		dataArgs.pop(0)
		self.requirements = []

		for index in range(len(dataArgs)):
			if dataArgs[index] == 1:
				self.requirements.append(givenArgs[0][index])


	def getName(self):
		return self.name


	def getRequirements(self):
		return self.requirements


	def isValid(self):
		return self.valid


	def output(self):
		output('\t' + self.name)
		output('\trequirements:')
		for requirement in self.requirements:
			requirement.output()