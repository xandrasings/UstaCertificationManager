from ..Classes.Achievement import *
from ..Classes.Requirement import *
from ..Classes.Discipline import *
from ..Classes.Official import *

acceptsDirectory = {
	'achievements' : True,
	'excel' : False,
	'officials' : False,
	'requirements' : False
}

colHeaderType = {
	'requirements' : Requirement,
	'officials' : Discipline
}

rowHeaderType = {
	'achievements' : Achievement,
	'officials' : Official,
	'requirements' : Discipline
}

expectedLeadingCols = {
	'achievements' : ['Last Name', 'First Name', 'Item Name', 'Item Started Date', 'Item Completed Date'],
	'requirements' : ['Discipline'],
	'officials' : ['First Name', 'Preferred Name', 'Last Name', 'Email']
}

expectedLeadingRows = {
	'achievements' : [],
	'requirements' : ['Discipline'],
	'officials' : ['First Name']
}

doPareColMax = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doPareRowMax = {
	'achievements' : False,
	'requirements' : True,
	'officials' : True
}

doValidateRanges = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateColHeaders = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateExpectedLeadingCols = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateColHeaderFormat = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateRowHeaders = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateExpectedLeadingRows = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateRowHeaderFormat = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateData = {
	'achievements' : True,
	'requirements' : True,
	'officials' : True
}

doValidateBinaryData = {
	'achievements' : False,
	'requirements' : True,
	'officials' : True
}

doValidateAchievementData = {
	'achievements' : True,
	'requirements' : False,
	'officials' : False
}