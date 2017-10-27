from .output import *

colorOptions = {
	'red' : '\033[95m',
	'blue' : '\033[94m',
	'green' : '\033[92m',
	'cyan' : '\033[96m',
	'yellow' : '\033[93m',
	'magenta' : '\033[95m',
	'black' : '\033[90m',
	'closer' : '\033[0m'
}

def color(text, color):
	return colorOptions[color] + text + colorOptions['closer']

def colorUserNotice(text):
	return colorOptions['green'] + text + colorOptions['closer']

def colorPrompt(text):
	return colorOptions['blue'] + text + colorOptions['closer']

def colorPromptImmediate(text):
	return colorOptions['blue'] + text + colorOptions['closer'] + colorOptions['magenta']

def colorClose():
	return colorOptions['closer']