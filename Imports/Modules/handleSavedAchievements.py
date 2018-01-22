from .selectData import *
from ..Classes.AchievementData import *
from ..Utilities.input import *
from ..Utilities.output import *

import csv
import os


def handleSavedAchievements(officials, requirements):
	dataType = 'saved achievements'
	targetDirectoryPath = extendPath(getAbsoluteFilePath('DataFiles'), 'backupData')
	ensureBackupDirectoryExists(targetDirectoryPath)
	achievements = set()

	backupOptions = getValidPathOptions(dataType, targetDirectoryPath, False)

	if len(backupOptions) > 0:
		if promptYN('Would you like to use most recently saved achievements data from ' + backupOptions[0] + '?'):
			achievements = loadSavedAchievements(officials, requirements, dataType, targetDirectoryPath, [backupOptions[0]])
		else:
			if(promptYN('Would you like to use other previously saved achievements data?')):
				achievements = loadSavedAchievements(officials, requirements, dataType, targetDirectoryPath, backupOptions)
	else:
		output('No previously saved achievements data available to load.')

	outputCloseModule(dataType)
	return achievements


def ensureBackupDirectoryExists(targetDirectoryPath):
	if not os.path.isdir(targetDirectoryPath):
		os.makedirs(targetDirectoryPath)
		output('Backup data directory was not found. Regenerating directory.')


def loadSavedAchievements(officials, requirements, dataType, targetDirectoryPath, backupOptions):
	
	backupFile = selectDataFiles(dataType, targetDirectoryPath, backupOptions)[0]

	achievements = set()
	achievementReader = csv.reader(open(backupFile, newline=''))
	for row in achievementReader:
		achievement = AchievementData(row, [officials, requirements])
		if achievement.isValid():
			achievements.add(achievement)

	return achievements