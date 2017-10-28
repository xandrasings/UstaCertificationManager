from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processDisciplineRequirements():
	data = selectDataSource('requirements')[0]
	data.setUp()

	requirements = data.convertCols()
	disciplines = data.convertRows([requirements])

	outputCloseModule('finished processing requirements data')
	return disciplines