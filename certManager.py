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

	options = {
		"A" : processAchievements,
		"D" : displayCertifications,
		"R" : displayRequirements,
		"O" : displayOfficial,
		"E" : sendEmails,
		"Q" : quit
	}

	displayOptions = True

	while (displayOptions == True):
		options["A"]()
		options["D"]()
		options["R"]()
		options["O"]()
		options["E"]()
		options["Q"]()
		displayOptions = False

main()