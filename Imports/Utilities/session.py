from colorama import init

def initialize():
	init()

def getTerminalWidth():
	import fcntl, termios, struct
	th, tw, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
	return tw