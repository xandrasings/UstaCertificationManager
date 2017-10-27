from .output import *

def prompt(text = ""):
	result = input(promptColor(text + " > "))
	closeColor()
	return result