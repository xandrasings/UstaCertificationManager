from .selectData import *
from ..Classes.DataAchievement import *
from ..Utilities.input import *
from ..Utilities.output import *

import csv

def loadSavedAchievements(officials, requirements):
	targetDirectoryPath = extendPath(getAbsoluteFilePath('DataFiles'), 'backupData')
	dataType = 'saved achievements'

	backupFile = selectDataFiles(dataType, targetDirectoryPath, False)[0]

	achievements = set()
	achievementReader = csv.reader(open(backupFile, newline=''))
	for row in achievementReader:
		achievement = DataAchievement(row, [officials, requirements])
		if achievement.isValid():
			achievements.add(achievement)

	outputCloseModule(dataType)
	return achievements