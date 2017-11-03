from .Achievement import *

class DataAchievement(Achievement):
	def __init__(self, dataArgs, givenArgs = []):
		self.official = None
		self.requirement = None

		for official in givenArgs[0]:
			if official.matches(getFullName(dataArgs[0], dataArgs[1])):
				self.official = official
				break

		for requirement in givenArgs[1]:
			if requirement.matches(dataArgs[2]):
				self.requirement = requirement
				break

		self.completedDate = dataArgs[3]
		self.sourceFile = dataArgs[4]
		self.valid = (
			isinstance(self.official, Official) and
			isinstance(self.requirement, Requirement)
		)