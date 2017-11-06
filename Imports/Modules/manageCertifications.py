from .displayAchievements import *
from .displayCertifications import *
from .displayIntroduction import *
from .displayOfficial import *
from .handleSavedAchievements import *
from .manageEmails import *
from .modifyAchievements import *
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
	achievements = handleSavedAchievements(officials, requirements)
	certifications = []

	while (True):
		selection = solicitAction()
		outputLine()
		if (selection == 'L'):
			achievements = achievements | processAchievements(targetDirectoryPath, officials, requirements)
		elif (selection == 'M'):
			achievements = modifyAchievements(achievements)
		elif (selection == 'S'):
			saveAchievements(achievements)
		elif (selection == 'C'):
			displayCertifications(certifications)
		elif (selection == 'A'):
			displayAchievements(requirements, officials, achievements)
		elif (selection == 'O'):
			displayOfficial(officials, disciplines, requirements, achievements, certifications)
		elif (selection == 'E'):
			manageEmails(officials, disciplines, requirements, achievements, certifications)
		elif (selection == 'Q'):
			quit()
		else:
			rejectOption(selection)