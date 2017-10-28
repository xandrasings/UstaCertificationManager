from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processDisciplineRequirements():
	data = selectDataSource('requirements')
	data.setUp()

	requirements = data.convertCols()
	disciplines = data.convertRows([requirements])

	print('requirements: ')
	for requirement in requirements:
		print(requirement.getName())

	print('disciplines: ')
	for discipline in disciplines:
		print(discipline.getName())
		for requirement in discipline.getRequirements():
			print(requirement.getName())
