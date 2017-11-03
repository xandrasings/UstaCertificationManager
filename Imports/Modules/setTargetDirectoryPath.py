from .quit import *
from .selectData import *
from ..Classes.Data import *
from ..Utilities.input import *
from ..Utilities.output import *
from ..Utilities.dataTypeRules import *

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

	if firstRun:
		output('Selected directory: ' + optionPath)
		outputCloseModule()

	return optionPath