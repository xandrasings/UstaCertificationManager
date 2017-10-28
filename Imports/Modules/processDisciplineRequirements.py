from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processDisciplineRequirements():
	dataType = 'requirements'
	data = selectDataSource(dataType)[0]
	data.setUp()

	requirements = data.convertCols()
	disciplines = data.convertRows([requirements])

	outputCloseProcessingModule(dataType)
	return [disciplines, requirements]