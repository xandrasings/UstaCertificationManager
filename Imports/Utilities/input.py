import sys

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
	selection = None
	while True:
		if selection is not None:
			outputUserNotice(selection + ' is not a valid response. Please enter \'Y\' or \'N\'')
		selection = prompt(text + ' (Y/N)')
		if selection == 'Y':
			return True
		elif selection == 'N':
			return False
		elif selection == 'Q':
			outputCloseApplication()
			sys.exit()


def promptContinue():
	input(colorPrompt('Press enter to continue. > '))
	outputCloseModule()


def rejectOption(selection):
	outputUserNotice('\'' + selection + '\' is not a viable option.')
	outputLine()