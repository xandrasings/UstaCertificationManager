from .displayAchievements import *
from .displayCertifications import *
from .displayIntroduction import *
from .displayOfficial import *
from .loadSavedAchievements import *
from .manageEmails import *
from .processAchievements import *
from .processOfficials import *
from .processDisciplineRequirements import *
from .quit import *
from .saveAchievements import *
from .setTargetDirectoryPath import *
from .solicitAction import *
from ..Utilities.output import *

def manageCertifications():
	displayIntroduction()
	targetDirectoryPath = setTargetDirectoryPath('DataFiles')
	pdr = processDisciplineRequirements(targetDirectoryPath)
	disciplines = pdr[0]
	requirements = pdr[1]
	officials = processOfficials(targetDirectoryPath, disciplines)
	achievements = set()
	certifications = []

	displayOptions = True;
	while (displayOptions == True):
		selection = solicitCertManagerAction()
		outputLine()
		if (selection == 'P'):
			achievements = achievements | loadSavedAchievements()
		elif (selection == 'L'):
			achievements = achievements | processAchievements(targetDirectoryPath, officials, requirements)
		elif (selection == 'M'):
			pass
		elif (selection == 'S'):
			saveAchievements(achievements)
		elif (selection == 'C'):
			displayCertifications(certifications);
		elif (selection == 'A'):
			displayAchievements(requirements, officials, achievements);
		elif (selection == 'O'):
			displayOfficial(officials, disciplines, requirements, achievements, certifications);
		elif (selection == 'E'):
			manageEmails(officials, disciplines, requirements, achievements, certifications)
		elif (selection == 'Q'):
			displayOptions = quit()
		else:
			rejectOption(selection)