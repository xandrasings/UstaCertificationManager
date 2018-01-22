from .selectData import *
from ..Utilities.input import *
from ..Utilities.output import *

def processAchievements(targetDirectoryPath, officials, requirements):
	dataType = 'achievements'
	achievements = set()
	for data in selectExcelData(dataType, targetDirectoryPath):
		if data.setUp():
			achievements = achievements | set(data.convertRows([officials, requirements]))
		else:
			# TODO
			output('something is AMISS')

	outputCloseModule(dataType)
	return achievements