from colorama import init
import sys

from .input import *
from .output import *

def initialize():
	init()

def getTerminalWidth():
	import fcntl, termios, struct
	th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
	return tw

def quit():
	outputCloseApplication()
	sys.exit()

def fatalQuit(exception):
	outputFatal(exception)
	quit()