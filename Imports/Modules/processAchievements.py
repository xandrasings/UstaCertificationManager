from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processAchievements(targetDirectoryPath, officials, requirements):
	dataType = 'achievements'
	achievements = []
	for data in selectDataSource(dataType, targetDirectoryPath):
		data.setUp()

		achievements.extend(data.convertRows([officials, requirements]))

	outputCloseProcessingModule(dataType)
	return achievements