import random


def generateDocID() :
	return chr(int(random.uniform(0,25.99)) + 97) + chr(int(random.uniform(0,25.99)) + 97) + chr(int(random.uniform(0,25.99)) + 97) + chr(int(random.uniform(0,9.99)) + 48) + chr(int(random.uniform(0,9.99)) + 48) + chr(int(random.uniform(0,9.99)) + 48) + chr(int(random.uniform(0,25.99)) + 97)