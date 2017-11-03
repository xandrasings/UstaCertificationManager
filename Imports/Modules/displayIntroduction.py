from ..Utilities.input import *
from ..Utilities.output import *

def displayIntroduction():
	clearTerminal()
	outputUserNotice('Welcome to Cert Manager.')
	output('I will help you manage certification requirements for USTA officials.')
	output('All source files must be in csv and should follow the expected format detailed in the readme.')
	output('See the readme for further details on source file requirements.')

	promptContinue()