from ..Utilities.input import *
from ..Utilities.output import *

def modifyAchievements(achievements):
	solicitModificationType()
	return achievements


def solicitModificationType():
	outputPrompt('What would you like to do?')
	outputOption(' - (A)dd a new reservation')
	outputOption(' - (M)odify an existing reservation')
	outputOption(' - (R)emove an existing reservation')
	outputOption(' - (Q)uit')
	return prompt()