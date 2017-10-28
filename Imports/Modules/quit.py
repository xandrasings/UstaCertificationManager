import sys

from ..Utilities.input import *
from ..Utilities.output import *

def quit():
	outputCloseApplication()
	sys.exit()


def fatalQuit(exception):
	outputFatal(exception)
	quit()