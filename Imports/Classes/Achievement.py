from .Official import *
from .Requirement import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Achievement:
	def __init__():
		pass

		
	def __eq__(self, other):
		return (
			isinstance(other, Achievement) and
			self.official.getName() == other.official.getName() and
			self.requirement.getName() == other.requirement.getName() and
			self.completedDate == other.completedDate and
			self.city == other.city and
			self.state == other.state and
			self.sourceFile == other.sourceFile
		)


	def __hash__(self):
		return hash(self.official.getName())


	def getOfficial(self):
		return self.official


	def getOfficialName(self):
		return self.official.getName()


	def getOfficialFirstName(self):
		return self.official.getFirstName()


	def getOfficialLastName(self):
		return self.official.getLastName()


	def getRequirement(self):
		return self.requirement


	def getRequirementName(self):
		return self.requirement.getName()


	def getCompletedDate(self):
		return self.completedDate


	def getCity(self):
		return self.city


	def getState(self):
		return self.state


	def getSourceFile(self):
		return self.sourceFile


	def isValid(self):
		return self.valid


	def output(self):
		output(self.official.getName())
		output(self.requirement.getName())
		output(self.completedDate)
		output(self.city)
		output(self.state)
		output(self.sourceFile)


def getFullName(firstName, lastName):
	return firstName + ' ' + lastName;