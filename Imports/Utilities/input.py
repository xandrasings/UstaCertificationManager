from .output import *

def prompt(text = '', default = ''):
	result = ''
	if default == '':
		result = input(colorPromptImmediate(text + ' > '))
	else:
		outputPrompt(text)
		result = input(colorPromptImmediate('enter \'Y\' for \'' + default + '\' > ')).upper()
		if result == 'Y':
			result = default
	outputColorClose()
	return result

def promptContinue():
	input(colorPrompt('Press enter to continue. > '))
	outputLineHeavy()