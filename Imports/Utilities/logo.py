from .color import *

logos = {
	'tennisBall' : '   ,odOO"bo,   \n' + ' ,dOOOP\'dOOOb, \n' + ',O3OP\'dOO3OO33,\n' + 'P",ad33O333O3Ob\n' + '?833O338333P",d\n' + '`88383838P,d38\'\n' + ' `Y8888P,d88P\' \n' + '   `"?8,8P"\'   '
	}

def processLogo(logo):
	return logos[logo].split('\n')
