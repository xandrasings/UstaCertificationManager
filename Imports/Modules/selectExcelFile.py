from ..Utilities.input import *
from ..Utilities.output import *

import os
from xlrd import open_workbook

def selectExcelFile(dataType, selectedFile = ''):
	output('Seeking excel file holding ' + dataType + ' data in Resources directory.')
	certificationDataFileName = prompt('Enter ' + dataType + ' file name', 'certificationData.xlsx')
	certificationDataFilePath = os.path.abspath(os.path.join('Resources', certificationDataFileName))
	# TODO change this to select from list of files
	certificationDataFile = open_workbook(certificationDataFilePath)

	return certificationDataFile