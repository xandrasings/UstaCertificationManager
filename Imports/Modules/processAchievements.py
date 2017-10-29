from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processAchievements(officials, requirements):
	dataType = 'achievements'
	data = selectDataSource(dataType)[0]
	data.setUp()

	achievements = data.convertRows([officials, requirements])

	outputCloseProcessingModule(dataType)
	return achievements