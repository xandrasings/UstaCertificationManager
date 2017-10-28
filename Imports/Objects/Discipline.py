from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Discipline:
	def __init__(self, dataArgs, givenArgs = []):
		self.name = dataArgs[0]
		del dataArgs[0]
		self.requirements = []

		for index in range(len(dataArgs)):
			if dataArgs[index] == 1:
				self.requirements.append(givenArgs[0][index])


	def getName(self):
		return self.name


	def getRequirements(self):
		return self.requirements