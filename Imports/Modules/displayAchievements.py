from ..Utilities.displayTable import *
from ..Utilities.input import *
from ..Utilities.output import *

def displayAchievements(requirements, officials, achievements):
	colHeaders = getItemNames(requirements)
	rowHeaders = getItemNames(officials)
	data = []

	tableCode = [
		['C',	'completed',		'green'],
		['N',	'not completed',	'black'],
	]
	meaningCode = {tableCodeItem[1]: tableCodeItem[0] for tableCodeItem in tableCode}

	for rowHeader in rowHeaders:
		newRow = []
		for colHeader in colHeaders:
			newRow.append(getTableValue(achievements, rowHeader, colHeader, meaningCode))
		data.append(newRow)

	displayTable(colHeaders, rowHeaders, data, tableCode)
	promptContinue()

def getItemNames(items):
	itemNames = []
	for item in items:
		itemNames.append(item.getName())

	return itemNames

def getTableValue(achievements, rowHeader, colHeader, meaningCode):
	tableValue = meaningCode['not completed']
	for achievement in achievements:
		if achievement.getOfficial().matches(rowHeader) and achievement.getRequirement().matches(colHeader):
			tableValue = meaningCode['completed']
			break
	return tableValue