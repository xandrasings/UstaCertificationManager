from .Achievement import *

class CourseAchievement(Achievement):
	def __init__(self, sourceFile, dataArgs, givenArgs = []):
		self.official = None
		self.requirement = None

		for official in givenArgs[0]:
			if official.matches(getFullName(dataArgs[1], dataArgs[0])):
				self.official = official
				break

		for requirement in givenArgs[1]:
			if requirement.matches(pare(dataArgs[2], [' course', '.','_OLD'])):
				self.requirement = requirement
				break

		self.completedDate = dataArgs[4]
		self.sourceFile = sourceFile
		self.valid = (
			isinstance(self.official, Official) and
			isinstance(self.requirement, Requirement) and
			len(self.completedDate) > 0
		)