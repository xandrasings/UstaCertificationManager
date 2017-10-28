from .quit import *
from .selectDataSource import *
from ..Utilities.input import *
from ..Utilities.output import *

def processOfficials(disciplines):
	data = selectDataSource('officials')[0]
	data.setUp()

	disciplines = checkMainColHeaders(disciplines, data.getMainColHeaders())
	officials = data.convertRows([disciplines])

	outputCloseModule('finished processing officials data')
	return officials

def checkMainColHeaders(disciplines, mainColHeaders):
	orderedDisciplines = []

	for header in mainColHeaders:
		found = False
		for discipline in disciplines:
			if discipline.getName() == header:
				found = True
				orderedDisciplines.append(discipline)
		if found == False:
			fatalQuit(
				'No discipline \'' + header + '\' was found in saved discipline list.\n' +
				'Be sure that all the discipline goals in the officials file are also present in the requirements file.'
			)

	return orderedDisciplines


