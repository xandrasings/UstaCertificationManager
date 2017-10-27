colorOptions = {
	"red" : '\033[95m',
	"blue" : '\033[94m',
	"green" : '\033[92m',
	"magenta" : '\033[95m',
	"closer" : '\033[0m'
}

def output(text, colorOption = "none"):
	if colorOption == "none":
		print(text)
	else:
		print(color(text, colorOption))

def outputUserNotice(text):
	print(colorUserNotice(text))

def color(text, color):
	return colorOptions[color] + text + colorOptions["closer"]

def colorUserNotice(text):
	return colorOptions["green"] + text + colorOptions["closer"]

def colorPrompt(text):
	return colorOptions["blue"] + text + colorOptions["closer"]

def colorPromptImmediate(text):
	return colorOptions["blue"] + text + colorOptions["closer"] + colorOptions["magenta"]

def colorClose():
	print(colorOptions["closer"])