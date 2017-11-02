
from .Official import *
from .Requirement import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Achievement:
	def __init__(self, sourceFile, dataArgs, givenArgs = []):
		self.official = None
		self.requirement = None

		for official in givenArgs[0]:
			if official.matches(getFullName(dataArgs[1], dataArgs[0])):
				self.official = official
				break

		for requirement in givenArgs[1]:
			if requirement.matches(pare(dataArgs[2], [' course', '.','_OLD'])):
				self.requirement = requirement
				break

		self.completedDate = dataArgs[4]
		self.sourceFile = sourceFile
		self.valid = (
			isinstance(self.official, Official) and
			isinstance(self.requirement, Requirement) and
			len(self.completedDate) > 0
		)


	def __eq__(self, other):
		return (
			isinstance(other, Achievement) and
			self.official.getName() == other.official.getName() and
			self.requirement.getName() == other.requirement.getName() and
			self.completedDate == other.completedDate
		)


	def __hash__(self):
		return hash(self.official.getName())


	def getOfficial(self):
		return self.official


	def getRequirement(self):
		return self.requirement


	def getValidity(self):
		return self.valid


	def output(self):
		output(self.official.getName())
		output(self.requirement.getName())
		output(self.completedDate)
		output(self.sourceFile)

def getFullName(firstName, lastName):
	return firstName + ' ' + lastName;