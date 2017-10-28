from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processAchievements(requirements):
	dataType = 'achievements'
	data = selectDataSource(dataType)[0]
	data.setUp()

	for requirement in requirements:
		print(requirement.getName())

	achievements = []

	outputCloseProcessingModule(dataType)
	return achievements