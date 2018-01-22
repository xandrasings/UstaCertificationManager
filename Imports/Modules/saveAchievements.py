from ..Modules.selectData import *
from ..Utilities.output import *

from datetime import datetime

import csv

def saveAchievements(achievements):
	backupFilePath = selectBackupFilePath()

	with open(backupFilePath, 'w', newline='') as backup:
		achievementWriter = csv.writer(backup, delimiter=',')
		for achievement in achievements:
			achievementWriter.writerow(generateRow(achievement))

	outputUserNotice('Current state of achievements is backed up to file ' + backupFilePath)
	outputCloseModule()


def selectBackupFilePath():
	backupFilePath = getAbsoluteFilePath('DataFiles')
	backupFilePath = extendPath(backupFilePath, 'backupData')
	backupFilePath = extendPath(backupFilePath, selectBackupFileName(backupFilePath))

	return backupFilePath


def selectBackupFileName(backupFilePath):
	dateString = getDateString()
	pathContent = listdir(backupFilePath)
	
	backupFileName = tryBackupFileName(dateString, 0, pathContent)

	return backupFileName


def getDateString():
	return str(datetime.now().date())


def tryBackupFileName(dateString, index, pathContent):
	backupFileName = generateBackupFileName(dateString, index)
	if backupFileName in pathContent:
		backupFileName = tryBackupFileName(dateString, index + 1, pathContent)

	return backupFileName


def generateBackupFileName(dateString, index):
	suffix = generateSuffix(index)
	return 'achievementsBackUp_' + dateString + suffix + '.csv'


def generateSuffix(index):
	suffix = ''
	
	if index > 0:
		suffix = str(index)
		if index < 10:
			suffix = '0' + suffix
		suffix = '_' + suffix	

	return suffix


def generateRow(achievement):
	row = []
	row.append(achievement.getOfficialFirstName())
	row.append(achievement.getOfficialLastName())
	row.append(achievement.getRequirementName())
	row.append(achievement.getCompletedDate())
	row.append(achievement.getCity())
	row.append(achievement.getState())
	row.append(achievement.getSourceFile())
	return row