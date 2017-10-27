from ..Utilities.input import *
from ..Utilities.output import *
from .quit import *

import os
from os import listdir
from xlrd import open_workbook

def selectExcelFile(dataType, selectedFile = ''):
	targetDirectory = 'Resources'

	certificationDataFilePath = getAbsoluteFilePath(targetDirectory)
	validOptions = getValidOptions(certificationDataFilePath)
	optionIndex = solicitOptionIndex(dataType, targetDirectory, validOptions)
	certificationDataFilePath = extendFilePath(certificationDataFilePath, validOptions[optionIndex])
	certificationDataFile = openWorkbook(certificationDataFilePath)

	return certificationDataFile

def printFileOptions(pathContent):
	i = 1
	for item in list(pathContent):
		outputOption('- (' + str(i) + ') ' + item)
		i = i + 1
	outputOption('- (Q)uit')

def getAbsoluteFilePath(filePath):
	return os.path.abspath(filePath)

def extendFilePath(filePath, extension):
	return os.path.join(filePath, extension)

def getValidOptions(filePath):
	pathContent = listdir(filePath)
	validOptions = filterExcelOptions(pathContent)

	return validOptions

def filterExcelOptions(pathContent):
	validOptions = []

	for item in list(pathContent):
		if (item.endswith('.xlsx') or item.endswith('.xls')) and not item.startswith('~'):
			validOptions.append(item)

	return validOptions

def solicitOptionIndex(dataType, targetDirectory, validOptions):
	output('Seeking excel file holding ' + dataType + ' data in ' + targetDirectory +' directory.')
	# TODO check if list is empty
	printFileOptions(validOptions)
	optionIndex = getFileIndex(dataType, validOptions)
	return optionIndex

def getFileIndex(dataType, validOptions):
	fileIndex = -1

	while fileIndex < 0:
		inputIndex = prompt('Which file would you like to use for ' + dataType + ' data?')
		try:
			fileIndex = int(inputIndex) - 1
			if fileIndex < 0 or fileIndex >= len(validOptions):
				outputUserNotice('Selection should be between 1 and ' + str(len(validOptions) + 1))
				fileIndex = -1
		except:
			if inputIndex == 'Q':
				quit()
			outputUserNotice('Selection should be an integer')

	return fileIndex

def openWorkbook(filePath):
	try:
		open_workbook(filePath)
		outputUserNotice('Opening workbook from ' + filePath)
	except:
		outputUserNotice('Could not open workbook')
		quit()
