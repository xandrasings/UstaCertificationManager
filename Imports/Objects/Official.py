from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Official:
	def __init__(self, dataArgs, givenArgs = []):
		self.firstName = dataArgs[0]
		self.lastName = dataArgs[1]
		self.emailAddress = dataArgs[2]
		del dataArgs[0]
		del dataArgs[0]
		del dataArgs[0]
		self.disciplines = []

		for index in range(len(dataArgs)):
			if dataArgs[index] == 1:
				self.disciplines.append(givenArgs[0][index])


	def getFirstName(self):
		return self.firstName

	def print(self):
		print('official:')
		print(self.firstName + ' ' + self.lastName)
		print(self.emailAddress)
		print('\tdisciplines:')

		for discipline in self.disciplines:
			print('\t\t' + discipline.getName())
			print('\t\trequirements:')
			for requirement in discipline.getRequirements():
				print('\t\t\t' + requirement.getName())