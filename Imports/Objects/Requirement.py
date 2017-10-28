from ..Utilities.dataTypeRules import *
from ..Utilities.output import *

class Requirement:
	def __init__(self, dataArgs, givenArgs = []):
		self.name = dataArgs[0]


	def getName(self):
		return self.name
