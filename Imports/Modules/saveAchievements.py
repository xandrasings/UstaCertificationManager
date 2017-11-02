from ..Modules.selectDataSource import *

from datetime import datetime

import csv

def saveAchievements(achievements):
	output('save achievements')
	backupFilePath = selectBackupFilePath()

	with open(backupFilePath, 'w', newline='') as backup:
		achievementWriter = csv.writer(backup, delimiter=',')
		achievementWriter.writerow([1,2,3,4,'5'])
		achievementWriter.writerow([1,2,3,4,'stringy, string, with, comments, in, it'])


def selectBackupFilePath():
	backupFilePath = getAbsoluteFilePath('DataFiles')
	backupFilePath = extendPath(backupFilePath, 'backupData')
	backupFilePath = extendPath(backupFilePath, selectBackupFileName(backupFilePath))

	return backupFilePath


def selectBackupFileName(backupFilePath):
	dateString = getDateString()
	backupFileName = generateBackupFileName(dateString)
	pathContent = listdir(backupFilePath)
	return backupFileName


def getDateString():
	return str(datetime.now().date())


def generateBackupFileName(dateString, suffix = ''):
	return 'achievementsBackUp_' + dateString + suffix + '.csv'