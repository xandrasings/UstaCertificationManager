from .color import *

logos = {
	'tennisBall' : '   ,odOO"bo,   \n' + ' ,dOOOP\'dOOOb, \n' + ',O3OP\'dOO3OO33,\n' + 'P",ad33O333O3Ob\n' + '?833O338333P",d\n' + '`88383838P,d38\'\n' + ' `Y8888P,d88P\' \n' + '   `"?8,8P"\'   '
	}

def processLogo(logo, reps):
	logo = logos[logo] # decode into logo
	logo = splitLogo(logo) # split into array of strings
	newLogo = ''
	logoIndex = 0
	while logoIndex < len(logo):
		count = 0
		while count < reps:
			newLogo = newLogo + logo[logoIndex] + '   '
			count = count + 1
		newLogo = newLogo + '\n'
		logoIndex = logoIndex + 1

	return newLogo


def splitLogo(logo):
	return logo.split('\n')
