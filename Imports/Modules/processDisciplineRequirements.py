from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processDisciplineRequirements(targetDirectoryPath):
	dataType = 'requirements'
	data = selectDataSource(dataType, targetDirectoryPath)[0]
	data.setUp()

	requirements = data.convertCols()
	disciplines = data.convertRows([requirements])

	outputCloseProcessingModule(dataType)
	return [disciplines, requirements]