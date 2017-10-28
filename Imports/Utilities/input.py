from .output import *

def prompt(text = '', default = ''):
	result = ''
	if default == '':
		result = input(colorPromptImmediate(text + ' > ')).upper()
	else:
		outputPrompt(text)
		result = input(colorPromptImmediate('enter \'Y\' for \'' + default + '\' > ')).upper()
		if result == 'Y':
			result = default
	outputColorClose()
	return result


def promptYN(text = ''):
	selection = ''
	while selection == '':
		selection = prompt(text + ' (Y/N)')
		if selection == 'Y':
			return True
		elif selection in ['N', 'Q']:
			return False
		else:
			selection = ''



def promptContinue():
	input(colorPrompt('Press enter to continue. > '))
	outputLineHeavy()


def rejectOption(selection):
	outputUserNotice('\'' + selection + '\' is not a viable option.')
	outputLine()