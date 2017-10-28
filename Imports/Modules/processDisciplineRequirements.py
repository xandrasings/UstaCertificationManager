from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processDisciplineRequirements():
	data = selectDataSource('requirements')
	data.setUp()

	requirements = data.convertCols()
	disciplines = data.convertRows([requirements])

	return disciplines
