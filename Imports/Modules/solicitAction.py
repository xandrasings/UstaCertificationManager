from ..Utilities.input import *
from ..Utilities.output import *

def solicitCertManagerAction():
	outputPrompt('What would you like to do?')
	outputOption(' - (L)oad new achievement data files')
	outputOption(' - (M)odify current state of achievements')
	outputOption(' - (S)ave current state of achievements')
	outputOption(' - Display (C)ertification table')
	outputOption(' - Display (A)chievement table')
	outputOption(' - Display (O)fficial details')
	outputOption(' - Send (E)mails')
	outputOption(' - (Q)uit')
	return prompt()