from ..Utilities.input import *
from ..Utilities.output import *

def solicitCertManagerAction():
	outputPrompt('What would you like to do?')
	outputOption(' - (L)oad previous state of achievements')
	outputOption(' - (E)nter new achievements')
	outputOption(' - (S)ave current state of achievements')
	outputOption(' - Display (C)ertification table')
	outputOption(' - Display (A)chievement table')
	outputOption(' - Display (O)fficial details')
	outputOption(' - Send e(M)ails')
	outputOption(' - (Q)uit')
	return prompt()