from .color import *
from .logo import *
from .session import *

import os

def clearTerminal():
	os.system('cls' if os.name == 'nt' else 'clear')

def output(text, colorOption = 'none'):
	if colorOption == 'none':
		print(text)
	else:
		print(color(text, colorOption))

def outputUserNotice(text):
	output(colorUserNotice(text))

def outputPrompt(text):
	output(colorPrompt(text))

def outputColorClose():
	output(colorClose())

def outputOption(text):
	leftIndex = text.index('(')
	rightIndex = text.index(')') + 1
	output(text[0:leftIndex] + colorPrompt(text[leftIndex:rightIndex]) + text[rightIndex:])

def outputCloseModule(dataType = None):
	if dataType is not None:
		output('finished processing ' + dataType +' data')
	outputLineHeavy()

def outputCloseApplication():
	outputUserNotice('Exiting Certification Manager.')
	outputLineHeavy()
	outputLogo('tennisBall', True, 'yellow')

def outputFatal(message):
	output(colorFatal(message))

def outputLine(basis = '-', colorOption = 'black'):
	reps = getTerminalWidth() // len(basis)
	outputString = ''
	while (reps > 0):
		outputString = outputString + basis
		reps -= 1
	output(outputString, colorOption)

def outputLineHeavy():
	outputLine('=')

def outputLogo(logo, repeated = False, colorOption = 'black'):
	logo = processLogo(logo)
	for line in logo:
		if repeated:
			outputLine(line + '  ', colorOption)
		else:
			output(line, colorOption)


