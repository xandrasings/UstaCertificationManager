from .selectDataSource import *
from ..Objects.Data import *
from ..Utilities.input import *
from ..Utilities.output import *

def processRequirements():
	data = selectDataSource('requirements')

	print(data.getColMax())
	print(data.getRowMax())
	data.startUp()
	print(data.getColMax())
	print(data.getRowMax())

	data.pareColMax()
	data.pareRowMax()
	data.validate()

