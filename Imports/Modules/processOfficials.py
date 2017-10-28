from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processOfficials():
	data = selectDataSource('officials')
	data.setUp()