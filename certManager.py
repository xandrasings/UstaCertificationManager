from Imports.Modules.displayAchievements import *
from Imports.Modules.displayCertifications import *
from Imports.Modules.displayIntroduction import *
from Imports.Modules.displayOfficial import *
from Imports.Modules.processAchievements import *
from Imports.Modules.processOfficials import *
from Imports.Modules.processRequirements import *
from Imports.Modules.rejectOption import *
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
		'E' : processAchievements,
		'C' : displayCertifications,
		'A' : displayAchievements,
		'O' : displayOfficial,
		'M' : sendEmails,
		'Q' : quit
	}

	acted = {
		'Q' : displayOptions
	}

	while (displayOptions == True):
		selection = solicitAction()
		if (selection == 'E'):
			achievements = processAchievements(achievements);
		elif (selection == 'C'):
			displayCertifications(certifications);
		elif (selection == 'A'):
			displayAchievements(achievements);
		elif (selection == 'O'):
			displayOfficial(officials, disciplines, requirements, achievements, certifications);
		elif (selection == 'M'):
			sendEmails(officials, disciplines, requirements, achievements, certifications)
		elif (selection == 'Q'):
			displayOptions = quit()
		else:
			rejectOption(selection)

main()