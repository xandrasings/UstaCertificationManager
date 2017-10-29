from .Official import *
from .Requirement import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Achievement:
	def __init__(self, dataArgs, givenArgs = []):
		self.official = None
		self.requirement = None

		for official in givenArgs[0]:
			if official.matches(dataArgs[1], dataArgs[0]):
				self.official = official
				break

		for requirement in givenArgs[1]:
			if requirement.matches(dataArgs[2]):
				self.requirement = requirement
				break

		self.completedDate = dataArgs[4]
		self.valid = isinstance(self.official, Official) and isinstance(self.requirement, Requirement)



	def getValidity(self):
		return self.valid


	def print(self):
		self.official.print()
		self.requirement.print()