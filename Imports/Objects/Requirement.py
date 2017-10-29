from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Requirement:
	def __init__(self, dataArgs, givenArgs = []):
		self.valid = True
		self.name = dataArgs[0]


	def getName(self):
		return self.name


	def getValidity(self):
		return self.valid


	def matches(self, name):
		return name == self.name


	def print(self):
		print('\t\t' + self.name)