from .color import *

logos = {
	'tennisBall' : '   ,odOO"bo,   \n' + ' ,dOOOP\'dOOOb, \n' + ',O3OP\'dOO3OO33,\n' + 'P",ad33O333O3Ob\n' + '?833O338333P",d\n' + '`88383838P,d38\'\n' + ' `Y8888P,d88P\' \n' + '   `"?8,8P"\'   '
	}

def processLogo(logo, reps):
	logo = logos[logo] # decode into logo
	logo = splitLogo(logo) # split into array of strings
	repeatedLogo = ''
	for logoIndex in range(len(logo)):
		count = 0
		while count < reps:
			repeatedLogo = repeatedLogo + logo[logoIndex] + '   '
			count = count + 1
		repeatedLogo = repeatedLogo + '\n'
		logoIndex = logoIndex + 1

	return repeatedLogo


def splitLogo(logo):
	return logo.split('\n')
