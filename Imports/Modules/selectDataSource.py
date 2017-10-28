from ..Utilities.input import *
from ..Utilities.output import *
from .quit import *

import os
from os import listdir
from xlrd import open_workbook

def selectDataSource(dataType):
	dataFile = selectExcelFile(dataType)


def selectExcelFile(dataType):
	targetDirectory = 'Resources'
	dataFilePath = getAbsoluteFilePath(targetDirectory)
	validOptions = getValidOptions(dataType, dataFilePath)
	optionIndex = solicitOptionIndex(dataType, targetDirectory, validOptions)
	dataFilePath = extendFilePath(dataFilePath, validOptions[optionIndex])
	dataFile = openWorkbook(dataFilePath)

	return dataFile


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


def getValidOptions(dataType, filePath):
	output('Seeking excel file holding ' + dataType + ' data in ' + filePath)
	pathContent = listdir(filePath)
	validOptions = filterExcelOptions(pathContent)

	if len(validOptions) == 0:
		emptyValidOptionAction = getEmptyValidOptionAction(filePath)
		return getValidOptions(dataType, filePath)

	return validOptions


def getEmptyValidOptionAction(filePath):
	outputUserNotice('No viable options were found in ' + filePath + '.')
	selection = ''

	while selection != 'T':
		outputPrompt('What would you like to do?')
		outputOption(' - (T)ry this directory again')
		outputOption(' - (Q)uit')
		selection = prompt()
		if selection == 'Q':
			quit()
		elif selection != 'T':
			rejectOption(selection)


def filterExcelOptions(pathContent):
	validOptions = []

	for item in list(pathContent):
		if (item.endswith('.xlsx') or item.endswith('.xls')) and not item.startswith('~'):
			validOptions.append(item)

	return validOptions


def solicitOptionIndex(dataType, targetDirectory, validOptions):
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
		fatalQuit('Could not open workbook')