from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Official:
	def __init__(self, dataArgs, givenArgs = []):
		self.valid = True
		self.firstName = dataArgs[0]
		self.lastName = dataArgs[1]
		self.emailAddress = dataArgs[2]
		dataArgs = dataArgs[3:]
		self.disciplines = []

		for index in range(len(dataArgs)):
			if dataArgs[index] == 1:
				self.disciplines.append(givenArgs[0][index])


	def getFirstName(self):
		return self.firstName


	def getLastName(self):
		return self.lastName


	def getFullName(self):
		return self.firstName + ' ' + self.lastName


	def getDisciplines(self):
		return self.disciplines


	def getValidity(self):
		return self.valid


	def matches(self, firstName, lastName):
		return firstName == self.firstName and lastName == self.lastName


	def output(self):
		output(self.getFullName())
		output(self.emailAddress)
		output('disciplines:')

		for discipline in self.disciplines:
			discipline.output()