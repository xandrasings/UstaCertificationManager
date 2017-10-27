from ..Utilities.input import *
from ..Utilities.output import *
from .quit import *

import os
from os import listdir
from xlrd import open_workbook

def selectExcelFile(dataType, selectedFile = ''):

	certificationDataFilePath = os.path.abspath(os.path.join('Resources','.'))
	pathContent = listdir(certificationDataFilePath)
	pathContentValid = []
	for item in list(pathContent):
		if (item.endswith('.xlsx') or item.endswith('.xls')) and not item.startswith('~'):
			pathContentValid.append(item)


	output('Seeking excel file holding ' + dataType + ' data in Resources directory.')
	# TODO check if list is empty
	printFileOptions(pathContentValid)

	fileIndex = -1

	while fileIndex < 0:
		inputIndex = prompt('Which file would you like to use for ' + dataType + ' data?')
		# TODO offer option to quit
		try:
			fileIndex = int(inputIndex) - 1
			if fileIndex < 0 or fileIndex >= len(pathContentValid):
				outputUserNotice('Selection should be between 1 and ' + str(len(pathContentValid) + 1))
				fileIndex = -1
		except:
			if inputIndex.upper() == 'Q':
				quit()
			outputUserNotice(inputIndex + ' should be an integer')

	certificationDataFilePath = os.path.join(certificationDataFilePath,pathContentValid[fileIndex])

	certificationDataFile = open_workbook(certificationDataFilePath)

	return certificationDataFile

def printFileOptions(pathContent):
	i = 1
	for item in list(pathContent):
		outputOption('- (' + str(i) + ') ' + item)
		i = i + 1
	outputOption('- (Q)uit')
