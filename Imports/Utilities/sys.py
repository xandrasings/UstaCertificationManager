import sys
from .output import *

def quit():
	outputCloseApplication()
	sys.exit()

def fatalQuit(exception):
	outputFatal(exception)
	quit()