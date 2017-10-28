from .selectDataSource import *
from ..Objects.Data import *
from ..Utilities.input import *
from ..Utilities.output import *

def processRequirements():
	data = selectDataSource('requirements')
	data.pareColMax()
	data.pareRowMax()
	data.validate()

