from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processAchievements(requirements):
	dataType = 'achievements'
	data = selectDataSource(dataType)[0]
	data.setUp()

	achievements = []

	outputCloseProcessingModule(dataType)
	return achievements