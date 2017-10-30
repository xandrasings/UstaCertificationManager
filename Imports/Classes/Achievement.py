
from .Official import *
from .Requirement import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Achievement:
	def __init__(self, dataArgs, givenArgs = []):
		self.official = None
		self.requirement = None

		if getFullName(dataArgs[1], dataArgs[0]) == "RICHARD ARIANS":
			print('Dick did:')
			print(dataArgs[2])

		for official in givenArgs[0]:
			if official.matches(getFullName(dataArgs[1], dataArgs[0])):
				self.official = official
				break

		for requirement in givenArgs[1]:
			if requirement.matches(pare(dataArgs[2], [' course', '.','_OLD'])):
				if getFullName(dataArgs[1], dataArgs[0]) == "RICHARD ARIANS":
					print('requirement match!')
				self.requirement = requirement
				break

		self.completedDate = dataArgs[4]
		self.valid = (
			isinstance(self.official, Official) and
			isinstance(self.requirement, Requirement) and
			len(self.completedDate) > 0
		)


	def getOfficial(self):
		return self.official


	def getRequirement(self):
		return self.requirement


	def getValidity(self):
		return self.valid


	def output(self):
		self.official.output()
		self.requirement.output()

def getFullName(firstName, lastName):
	return firstName + ' ' + lastName;