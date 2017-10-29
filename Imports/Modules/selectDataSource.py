from .quit import *
from ..Classes.Data import *
from ..Utilities.input import *
from ..Utilities.output import *
from ..Utilities.dataTypeRules import *

import os
from os import listdir
from xlrd import *

def selectDataSource(dataType):
	dataFilePaths = selectDataFiles(dataType) # I'm a list now
	data = getDataFiles(dataType, dataFilePaths)
	
	return data


def selectDataFiles(dataType):
	targetDirectory = 'Resources'
	dataFilePath = getAbsoluteFilePath(targetDirectory)
	validOptions = getValidFileOptions(dataType, dataFilePath)
	optionIndex = solicitFileOptionIndex(dataType, targetDirectory, validOptions)
	optionPath = extendPath(dataFilePath, validOptions[optionIndex])
	dataFilePaths = getFilePaths(optionPath)

	return dataFilePaths


def getAbsoluteFilePath(filePath):
	return os.path.abspath(filePath)


def getValidFileOptions(dataType, filePath):
	output('Seeking excel file holding ' + dataType + ' data in ' + filePath)
	pathContent = listdir(filePath)
	validOptions = filterFileOptions(dataType, pathContent)

	if len(validOptions) == 0:
		emptyValidOptionAction = showEmptyValidOptionActions(filePath)
		validOptions = getValidFileOptions(dataType, filePath)

	return validOptions


def filterFileOptions(dataType, pathContent):
	validOptions = []

	for item in list(pathContent):
		if (
			(
				(
					item.endswith('.xlsx') or
					item.endswith('.xls')
				) and
				(	
					not item.startswith('~')
				)
			) or
			(
				('.' not in item) if acceptsDirectory[dataType] else False
			)
		):
			validOptions.append(item)

	return validOptions


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


def solicitFileOptionIndex(dataType, targetDirectory, validOptions):
	printFileOptions(dataType, validOptions)
	optionIndex = getFileIndex(validOptions)
	return optionIndex


def printFileOptions(dataType, pathContent):
	outputPrompt('Which file or directory would you like to use for ' + dataType + ' data?')
	i = 1
	for item in list(pathContent):
		outputOption('- (' + str(i) + ') ' + item)
		i = i + 1
	outputOption('- (Q)uit')


def getFileIndex(validOptions):
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
	return os.path.join(filePath, extension)


def getFilePaths(optionPath):
	filePaths = []

	if (
		optionPath.endswith('.xlsx') or
		optionPath.endswith('.xls')
		):
		filePaths.append(optionPath)
	else:
		validFileOptions = getValidFileOptions('excel', optionPath)
		for validFile in validFileOptions:
			filePaths.append(extendPath(optionPath, validFile))

	return filePaths


def getDataFiles(dataType, dataFilePaths):
	data = []
	for dataFilePath in dataFilePaths:
		dataFile = openWorkbook(dataFilePath)
		dataSheetIndex = selectDataSheetIndex(dataFile)
		data.append(Data(dataFile.sheet_by_index(dataSheetIndex), dataType))

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
