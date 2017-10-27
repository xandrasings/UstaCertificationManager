from .output import *

def prompt(text = ""):
	result = input(colorPromptImmediate(text + " > "))
	colorClose()
	return result