from .quit import *
from ..Utilities.input import *
from ..Utilities.output import *

def modifyAchievements(achievements):


	displayOptions = True;
	while (displayOptions):
		selection = solicitModificationType()
		if (selection == 'A'):
			output('add')
			displayOptions = offerNewModification()
		elif (selection == 'M'):
			output('modify')
			displayOptions = offerNewModification()
		elif (selection == 'R'):
			output('remove')
			displayOptions = offerNewModification()
		elif (selection == 'Q'):
			quit()
		else:
			rejectOption(selection)

	return achievements


def solicitModificationType():
	outputPrompt('What would you like to do?')
	outputOption(' - (A)dd a new reservation')
	outputOption(' - (M)odify an existing reservation')
	outputOption(' - (R)emove an existing reservation')
	outputOption(' - (Q)uit')
	return prompt()

def offerNewModification():
	return promptYN('Would you like to make another modification?')