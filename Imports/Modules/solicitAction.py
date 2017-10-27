from ..Utilities.input import *
from ..Utilities.output import *

def solicitAction():
	outputPrompt('What would you like to do?')
	outputOption(' - (E)nter new Achievements')
	outputOption(' - display (C)ertification table')
	outputOption(' - display (A)chievement table')
	outputOption(' - display (O)fficial details')
	outputOption(' - send e(M)ails')
	outputOption(' - (Q)uit')
	return prompt()