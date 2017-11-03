from .selectData import *
from ..Utilities.input import *
from ..Utilities.output import *

import csv

def loadSavedAchievements():
	targetDirectoryPath = extendPath(getAbsoluteFilePath('DataFiles'), 'backupData')
	dataType = 'saved achievements'

	backupFile = selectDataFiles(dataType, targetDirectoryPath, False)[0]

	achievements = set()
	achievementReader = csv.reader(open(backupFile, newline=''))
	for row in achievementReader:
		print(', '.join(row))

		# achievements = achievements | set(data.convertRows([officials, requirements]))

	outputCloseModule(dataType)
	return achievements