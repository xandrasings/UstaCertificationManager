colorOptions = {
	"red" : '\033[95m',
	"blue" : '\033[94m',
	"green" : '\033[92m',
	"closer" : '\033[0m'
}

def color(text, color):
	return colorOptions[color] + text + colorOptions["closer"]

def promptColor(text):
	return colorOptions["blue"] + text + colorOptions["closer"] + colorOptions["green"]

def closeColor():
	print(colorOptions["closer"])

def output(text, colorOption = "none"):
	if colorOption == "none":
		print(text)
	else:
		print(color(text, colorOption))