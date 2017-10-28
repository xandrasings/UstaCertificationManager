import sys

from ..Utilities.input import *
from ..Utilities.output import *

def quit():
	outputUserNotice('Exiting certification manager.')
	outputLineHeavy()
	outputLogo('tennisBall', 8, 'yellow')
	sys.exit()


def fatalQuit(exception):
	outputFatal(exception)
	quit()