from ..Utilities.input import *
from ..Utilities.output import *

def solicitCertManagerAction():
	outputPrompt('What would you like to do?')
	outputOption(' - (E)nter new achievements')
	outputOption(' - Display (C)ertification table')
	outputOption(' - Display (A)chievement table')
	outputOption(' - Display (O)fficial details')
	outputOption(' - Send e(M)ails')
	outputOption(' - (S)ave current achievements')
	outputOption(' - (Q)uit')
	return prompt()