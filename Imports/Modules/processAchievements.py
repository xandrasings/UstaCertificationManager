from ..Utilities.input import *
from ..Utilities.output import *

def processAchievements(requirements):
	data = selectDataSource('achievements')[0]
	data.setUp()

	achievements = []

	outputCloseModule('finished processing achievements data')
	return achievements