from Modules.displayCertifications import *
from Modules.displayIntroduction import *
from Modules.displayOfficial import *
from Modules.displayRequirements import *
from Modules.processAchievements import *
from Modules.processOfficials import *
from Modules.processRequirements import *
from Modules.quit import *
from Modules.sendEmails import *

def main():
	officials = []
	disciplines = []
	requirements = []
	achievements = []
	certifications = []

	displayIntroduction()
	processRequirements()
	processOfficials()

	displayOptions = True

	while (displayOptions == True):
		processAchievements()
		displayCertifications()
		displayRequirements()
		displayOfficial()
		sendEmails()
		quit()
		displayOptions = False

main()