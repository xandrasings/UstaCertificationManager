from ..Objects.Requirement import *
from ..Objects.Discipline import *
from ..Objects.Official import *

acceptsDirectory = {
	'requirements' : False,
	'officials' : False,
	'achievements' : True,
}


colHeaderType = {
	'requirements' : Requirement,
	'officials' : Discipline
}

rowHeaderType = {
	'requirements' : Discipline,
	'officials' : Official
}

doPareColMax = {
	'requirements' : True,
	'officials' : True
}

doPareRowMax = {
	'requirements' : True,
	'officials' : True
}

doValidateRanges = {
	'requirements' : True,
	'officials' : True
}

expectedHeaderRows = {
	'requirements' : 1,
	'officials' : 1
}

expectedHeaderCols = {
	'requirements' : 1,
	'officials' : 1
}

doValidateColHeaders = {
	'requirements' : True,
	'officials' : True
}

expectedLeadingCols = {
	'requirements' : ['Discipline'],
	'officials' : ['First Name', 'Last Name', 'Email']
}

doValidateExpectedLeadingCols = {
	'requirements' : True,
	'officials' : True
}

doValidateColHeaderFormat = {
	'requirements' : True,
	'officials' : True
}

doValidateRowHeaders = {
	'requirements' : True,
	'officials' : True
}

expectedLeadingRows = {
	'requirements' : ['Discipline'],
	'officials' : ['First Name']
}

doValidateExpectedLeadingRows = {
	'requirements' : True,
	'officials' : True
}

doValidateRowHeaderFormat = {
	'requirements' : True,
	'officials' : True
}

doValidateData = {
	'requirements' : True,
	'officials' : True
}