def color(text, color):

	closer = '\033[0m'

	colorOptions = {
		"red" : '\033[95m',
		"blue" : '\033[94m',
		"green" : '\033[92m',
	}

	return colorOptions[color] + text + closer

def output(text, colorOption = "none"):
	if colorOption == "none":
		print(text)
	else:
		print(color(text, colorOption))