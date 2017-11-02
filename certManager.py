from Imports.Modules.displayAchievements import *
from Imports.Modules.displayCertifications import *
from Imports.Modules.displayIntroduction import *
from Imports.Modules.displayOfficial import *
from Imports.Modules.manageEmails import *
from Imports.Modules.processAchievements import *
from Imports.Modules.processOfficials import *
from Imports.Modules.processDisciplineRequirements import *
from Imports.Modules.setTargetDirectoryPath import *
from Imports.Modules.quit import *
from Imports.Modules.solicitAction import *

def main():
	displayIntroduction()
	targetDirectoryPath = setTargetDirectoryPath('DataFiles')
	pdr = processDisciplineRequirements(targetDirectoryPath)
	disciplines = pdr[0]
	requirements = pdr[1]
	officials = processOfficials(targetDirectoryPath, disciplines)
	achievements = []
	certifications = []

	displayOptions = True;
	while (displayOptions == True):
		selection = solicitCertManagerAction()
		if (selection == 'E'):
			achievements.extend(processAchievements(targetDirectoryPath, officials, requirements));
		elif (selection == 'C'):
			displayCertifications(certifications);
		elif (selection == 'A'):
			displayAchievements(requirements, officials, achievements);
		elif (selection == 'O'):
			displayOfficial(officials, disciplines, requirements, achievements, certifications);
		elif (selection == 'M'):
			manageEmails(officials, disciplines, requirements, achievements, certifications)
		elif (selection == 'Q'):
			displayOptions = quit()
		else:
			rejectOption(selection)
			
main()