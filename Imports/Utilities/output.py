from .color import *
from .logo import *

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

def outputCloseModule(message):
	output(message)
	outputLine()

def outputCloseApplication():
	outputUserNotice('Exiting Certification Manager.')
	outputLineHeavy()
	outputLogo('tennisBall', 8, 'yellow')

def outputFatal(message):
	output(colorFatal(message))

def outputLine():
	output('--------------------------------------------------------------------------------------------------------------------------------------------')

def outputLineHeavy():
	output('============================================================================================================================================')

def outputLogo(logo, reps = 1, colorOption = 'black'):
	logo = processLogo(logo, reps)
	output(color(logo,colorOption))





