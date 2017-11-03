from .selectData import *
from ..Utilities.input import *
from ..Utilities.output import *

def processDisciplineRequirements(targetDirectoryPath):
	dataType = 'requirements'
	data = selectExcelData(dataType, targetDirectoryPath)[0]
	data.setUp()

	requirements = data.convertCols()
	disciplines = data.convertRows([requirements])

	outputCloseModule(dataType)
	return [disciplines, requirements]