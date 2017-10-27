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

	displayOptions = True

	options = {
		'A' : processAchievements,
		'D' : displayCertifications,
		'R' : displayRequirements,
		'O' : displayOfficial,
		'E' : sendEmails,
		'Q' : quit
	}

	acted = {
		'Q' : displayOptions
	}

	while (displayOptions == True):
		selection = solicitAction()
		if selection in options:
			acted[selection] = options[selection]()
		else:
			outputUserNotice('\'' + selection + '\' is not a viable option.')
			displayOptions = False

main()