from ..Utilities.displayTable import *
from ..Utilities.input import *
from ..Utilities.output import *

def displayAchievements(requirements, officials, achievements):
	outputLine()
	colHeaders = []
	rowHeaders = []
	data = []

	for achievement in achievements:
		achievement.output()

	rowHeaders = getItemNames(requirements)
	colHeaders = getItemNames(officials)

	for rowHeader in rowHeaders:
		newRow = []
		for colHeader in colHeaders:
			newCell = 'C'
			newRow.append(getTableValue(achievements, rowHeader, colHeader))
		data.append(newRow)

	displayTable(colHeaders, rowHeaders, data)
	outputLineHeavy()
	promptContinue()

def getItemNames(items):
	itemNames = []
	for item in items:
		itemNames.append(item.getName())

	return itemNames

def getTableValue(achievements, rowHeader, colHeader):
	tableValue = 'N'
	for achievement in achievements:
		if achievement.getOfficial().matches(colHeader) and achievement.getRequirement().matches(rowHeader):
			tableValue = 'C'
			break
	return tableValue