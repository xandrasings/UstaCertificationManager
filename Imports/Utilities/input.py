from .output import *

def prompt(text = ''):
	result = input(colorPromptImmediate(text + ' > '))
	colorClose()
	return result

def promptContinue():
	input(colorPrompt('Press enter to continue. > '))
	# TODO print line