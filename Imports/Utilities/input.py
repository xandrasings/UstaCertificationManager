from .output import *

def prompt(text = ''):
	result = input(colorPromptImmediate(text + ' > '))
	outputColorClose()
	return result

def promptContinue():
	input(colorPrompt('Press enter to continue. > '))
	outputLineHeavy()