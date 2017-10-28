from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

from xlrd import open_workbook

def processOfficials():
	data = selectDataSource('officials')
	data.startUp()