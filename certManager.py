from Imports.Modules.displayCertifications import *
from Imports.Modules.displayIntroduction import *
from Imports.Modules.displayOfficial import *
from Imports.Modules.displayRequirements import *
from Imports.Modules.processAchievements import *
from Imports.Modules.processOfficials import *
from Imports.Modules.processRequirements import *
from Imports.Modules.quit import *
from Imports.Modules.sendEmails import *
from Imports.Modules.solicitAction import *
from Imports.Utilities.input import *
from Imports.Utilities.output import *

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
		solicitAction()
		options["A"]()
		options["D"]()
		options["R"]()
		options["O"]()
		options["E"]()
		options["Q"]()
		displayOptions = False

main()