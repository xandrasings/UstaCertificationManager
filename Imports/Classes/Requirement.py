from .Helpers.DataHelper import *
from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Requirement:
	def __init__(self, sourceFile, dataArgs, givenArgs = []):
		self.valid = True
		self.name = pare(dataArgs[0], [' course'])


	def getName(self):
		return self.name


	def getValidity(self):
		return self.valid


	def matches(self, name):
		return name == self.name


	def output(self):
		output('\t\t' + self.name)