from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Achievement:
	def __init__(self, dataArgs, givenArgs = []):
		print('processing data line: ' + dataArgs[0] + ', ' + dataArgs[1] + ', ' + dataArgs[2])
		officials = givenArgs[0]
		requirements = givenArgs[1] #remove

		foundOfficial = False
		foundRequirement = False

		self.official = None
		self.requirement = None

		for official in officials:
			if official.matches(dataArgs[1], dataArgs[0]):
				self.official = official
				foundOfficial = True
				break

		for requirement in requirements:
			if requirement.matches(dataArgs[2]):
				self.requirement = requirement
				foundRequirement = True
				break



			# change me to check type
		self.completedDate = dataArgs[4]
		self.valid = foundOfficial and foundRequirement



	def getValidity(self):
		return self.valid


	def print(self):
		self.official.print()
		self.requirement.print()