from colorama import Fore, Style

colorOptions = {
	'red' : Fore.RED + Style.BRIGHT,
	'blue' : Fore.BLUE + Style.BRIGHT,
	'green' : Fore.GREEN + Style.BRIGHT,
	'cyan' : Fore.CYAN + Style.BRIGHT,
	'yellow' : '\033[93m' + Style.BRIGHT,
	'magenta' : Fore.MAGENTA,
	'black' : Fore.BLACK,
	'closer' : Style.RESET_ALL
}

def color(text, color):
	return colorOptions[color] + text + colorOptions['closer']

def colorUserNotice(text):
	return colorOptions['green'] + text + colorOptions['closer']

def colorPrompt(text):
	return colorOptions['blue'] + text + colorOptions['closer']

def colorPromptImmediate(text):
	return colorOptions['blue'] + text + colorOptions['closer'] + colorOptions['magenta']

def colorFatal(text):
	return colorOptions['red'] + text + colorOptions['closer']

def colorClose():
	return colorOptions['closer']