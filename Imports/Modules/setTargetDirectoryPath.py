from .quit import *
from ..Classes.Data import *
from ..Modules.selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *
from ..Utilities.dataTypeRules import *

import os
from os import listdir

def setTargetDirectoryPath(targetDirectoryPath, firstRun = True):
	targetDirectoryPath = getAbsoluteFilePath(targetDirectoryPath)
	if firstRun:
		outputUserNotice('Navigate to the directory where any new data input is stored.')
	output('Current directory: ' + targetDirectoryPath)

	dataType = 'directory'
	validOptions = getValidPathOptions(dataType, targetDirectoryPath)
	optionIndex = solicitPathOptionIndex(validOptions)
	optionPath = extendPath(targetDirectoryPath, validOptions[optionIndex])

	if optionPath != targetDirectoryPath:
		optionPath = setTargetDirectoryPath(optionPath, False)
	output('Selected directory: ' + optionPath)
	return optionPath


def getAbsoluteFilePath(filePath):
	return os.path.abspath(filePath)