import random
f=open('aaabbb.txt','r')
print(f)
def random_line():
	lines = open('aaabbb.txt').read().splitlines()
	return random.choice(lines)
print(random_line())