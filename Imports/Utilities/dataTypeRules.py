from .fileSort import *
from ..Classes.Achievement import *
from ..Classes.AchievementCourseType1 import *
from ..Classes.AchievementCourseType2 import *
from ..Classes.AchievementVision import *
from ..Classes.Requirement import *
from ..Classes.Discipline import *
from ..Classes.Official import *

displayNavigationPrompt = {
	'achievements' : True,
	'directory' : True,
	'excelFile' : True,
	'officials' : True,
	'requirements' : True,
	'saved achievements' : False
}

defaultsToSoleOption = {
	'achievements' : False,
	'directory' : False,
	'excelFile' : False,
	'officials' : False,
	'requirements' : False,
	'saved achievements' : True
}

acceptsSelf = {
	'achievements' : False,
	'directory' : True,
	'excelFile' : False,
	'officials' : False,
	'requirements' : False,
	'saved achievements' : False
}

acceptsDirectory = {
	'achievements' : True,
	'directory' : True,
	'excelFile' : False,
	'officials' : False,
	'requirements' : False,
	'saved achievements' : False
}

acceptsExcelFile = {
	'achievements' : True,
	'directory' : False,
	'excelFile' : True,
	'officials' : True,
	'requirements' : True,
	'saved achievements' : False
}

acceptsCsvFile = {
	'achievements' : False,
	'directory' : False,
	'excelFile' : False,
	'officials' : False,
	'requirements' : False,
	'saved achievements' : True
}


sortType = {
	'achievements' : noSort,
	'directory' : noSort,
	'excelFile' : noSort,
	'officials' : noSort,
	'requirements' : noSort,
	'saved achievements' : reverseAlphaSort
}

colHeaderType = {
	'requirements' : Requirement,
	'officials' : Discipline
}

rowHeaderType = {
	'course achievements type 1' : AchievementCourseType1,
	'course achievements type 2' : AchievementCourseType2,
	'officials' : Official,
	'requirements' : Discipline,
	'vision achievements' : AchievementVision
}

expectedLeadingCols = {
	'course achievements type 1' : ['Last Name', 'First Name', 'Item Name', 'Item Started Date', 'Item Completed Date', 'City', 'State/Province'],
	'course achievements type 2' : ['Last Name', 'First Name', 'Item Name', 'Item Started Date', 'Item Completed Date', 'Item Status', 'City', 'State/Province'],
	'requirements' : ['Discipline'],
	'officials' : ['First Name', 'Preferred Name', 'Last Name', 'Email'],
	'vision achievements' : ['For Year', 'Last Name', 'First Name', 'Certification Button', 'Vision Received', 'Email', 'District', 'Section', 'Notes']
}

typeParents = {
	'course achievements type 1' : 'achievements',
	'course achievements type 2' : 'achievements',
	'requirements' : 'requirements',
	'officials' : 'officials',
	'vision achievements' : 'achievements'
}

expectedLeadingRows = {
	'course achievements type 1' : [],
	'course achievements type 2' : [],
	'requirements' : ['Discipline'],
	'officials' : ['First Name'],
	'vision achievements' : []
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
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateColHeaders = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateExpectedLeadingCols = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateColHeaderFormat = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateRowHeaders = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateExpectedLeadingRows = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateRowHeaderFormat = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateData = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : True
}

doValidateBinaryData = {
	'course achievements type 1' : False,
	'course achievements type 2' : False,
	'requirements' : True,
	'officials' : True,
	'vision achievements' : False
}

doValidateAchievementData = {
	'course achievements type 1' : True,
	'course achievements type 2' : True,
	'requirements' : False,
	'officials' : False,
	'vision achievements' : False
}