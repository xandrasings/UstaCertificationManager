from .quit import *
from ..Classes.Data import *
from ..Utilities.input import *
from ..Utilities.output import *
from ..Utilities.dataTypeRules import *

from os import listdir
from xlrd import *

import os

def selectDataSource(dataType, targetDirectoryPath):
	dataFilePaths = selectDataFiles(dataType, targetDirectoryPath)
	data = getDataFiles(dataType, dataFilePaths)
	
	return data


def selectDataFiles(dataType, targetDirectoryPath):
	output('Seeking file holding ' + dataType + ' data in ' + targetDirectoryPath)
	validOptions = getValidPathOptions(dataType, targetDirectoryPath)
	outputPrompt('Which file or directory would you like to use for ' + dataType + ' data?')
	optionIndex = solicitPathOptionIndex(validOptions)
	optionPath = extendPath(targetDirectoryPath, validOptions[optionIndex])
	dataFilePaths = getFilePaths(optionPath)

	return dataFilePaths


def getValidPathOptions(dataType, filePath):
	pathContent = listdir(filePath)
	validOptions = filterPathOptions(dataType, pathContent)

	if len(validOptions) == 0:
		emptyValidOptionAction = showEmptyValidOptionActions(filePath)
		validOptions = getValidPathOptions(dataType, filePath)

	return validOptions


def filterPathOptions(dataType, pathContent):
	validOptions = []

	if acceptsSelf[dataType]:
		validOptions.append('current directory')

	for item in list(pathContent):
		if ((acceptsDirectory[dataType] and isValidDirectory(item)) or
		(acceptsExcelFile[dataType] and isValidExcelFile(item))):
			validOptions.append(item)

	return validOptions


def isValidDirectory(item):
	return '.' not in item and item != 'backupData'


def isValidExcelFile(item):
	status = (
		(
			item.endswith('.xlsx') or
			item.endswith('.xls')
		) and (	
			not item.startswith('~')
		)
	)
	return status


def showEmptyValidOptionActions(filePath):
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


def solicitPathOptionIndex(validOptions):
	printPathOptions(validOptions)
	optionIndex = getPathIndex(validOptions)
	return optionIndex


def printPathOptions(pathContent):
	i = 1
	for item in list(pathContent):
		outputOption('- (' + str(i) + ') ' + item)
		i = i + 1
	outputOption('- (Q)uit')


def getPathIndex(validOptions):
	fileIndex = -1
	maxInput = len(validOptions)

	while fileIndex < 0:
		inputIndex = prompt()
		try:
			fileIndex = int(inputIndex) - 1
			if fileIndex < 0 or fileIndex >= maxInput:
				outputUserNotice('Selection should be between 1 and ' + str(maxInput))
				fileIndex = -1
		except:
			if inputIndex == 'Q':
				quit()
			outputUserNotice('Selection should be an integer')

	return fileIndex


def extendPath(filePath, extension):
	if extension != 'current directory':
		filePath = os.path.join(filePath, extension)
	return filePath


def getFileName(filePath):
	return os.path.basename(filePath)


def getAbsoluteFilePath(filePath):
	return os.path.abspath(filePath)


def getFilePaths(optionPath):
	filePaths = []

	if (
		optionPath.endswith('.xlsx') or
		optionPath.endswith('.xls')
		):
		filePaths.append(optionPath)
	else:
		validFileOptions = getValidPathOptions('excelFile', optionPath)
		for validFile in validFileOptions:
			filePaths.append(extendPath(optionPath, validFile))

	return filePaths


def getDataFiles(dataType, dataFilePaths):
	data = []
	for dataFilePath in dataFilePaths:
		dataFile = openWorkbook(dataFilePath)
		dataSheetIndex = selectDataSheetIndex(dataFile)
		data.append(Data(dataFile.sheet_by_index(dataSheetIndex), dataType, getFileName(dataFilePath)))

	return data


def openWorkbook(filePath):
	dataFile = ''
	try:
		dataFile = open_workbook(filePath, on_demand = True)
		output('Selected workbook: ' + filePath + '.')
	except:
		fatalQuit('Could not open workbook')

	return dataFile


def selectDataSheetIndex(dataFile):
	sheetIndex = 0
	sheetOptions = dataFile.sheet_names()
	if len(sheetOptions) != 1:
		sheetIndex = solicitSheetOptionIndex(sheetOptions)

	output('Selected sheet: \'' + sheetOptions[sheetIndex] + '\'.')
	return sheetIndex


def solicitSheetOptionIndex(validOptions):
	printSheetOptions(validOptions)
	optionIndex = getSheetIndex(validOptions)
	return optionIndex


def printSheetOptions(validOptions):
	outputPrompt('Which sheet would you like to use?')
	i = 1
	for item in list(validOptions):
		outputOption('- (' + str(i) + ') ' + item)
		i = i + 1
	outputOption('- (Q)uit')


def getSheetIndex(validOptions):
	sheetIndex = -1
	maxInput = len(validOptions)

	while sheetIndex < 0:
		inputIndex = prompt()
		try:
			sheetIndex = int(inputIndex) - 1
			if sheetIndex < 0 or sheetIndex >= maxInput:
				outputUserNotice('Selection should be between 1 and ' + str(maxInput))
				sheetIndex = -1
		except:
			if inputIndex == 'Q':
				quit()
			outputUserNotice('Selection should be an integer')

	return sheetIndex
