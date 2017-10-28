from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processRequirements():
	data = selectDataSource('requirements')
	data.setUp()

