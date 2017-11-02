from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Official:
	def __init__(self, sourceFile, dataArgs, givenArgs = []):
		self.valid = True
		self.firstName = dataArgs[0]
		self.preferredName = dataArgs[1]
		self.lastName = dataArgs[2]
		self.emailAddress = dataArgs[3]
		dataArgs = dataArgs[4:]
		self.disciplines = []
		self.achievements = []

		for index in range(len(dataArgs)):
			if dataArgs[index] == 1:
				self.disciplines.append(givenArgs[0][index])


	def getFirstName(self):
		return self.firstName


	def getLastName(self):
		return self.lastName


	def getPreferredName(self):
		return (self.firstName if len(self.preferredName) == 0 else self.preferredName) + ' ' + self.lastName


	def getName(self):
		return self.firstName + ' ' + self.lastName


	def getDisciplines(self):
		return self.disciplines


	def getValidity(self):
		return self.valid


	def matches(self, name):
		return name == self.getName()


	def output(self):
		output(self.getName())
		output(self.emailAddress)
		output('disciplines:')

		for discipline in self.disciplines:
			discipline.output()