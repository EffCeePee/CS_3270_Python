
territoriesFile = open('territories.txt')
gameStateFile = open('gameState.txt')
tline = territoriesFile.readline()
sline = gameStateFile.readline()
# temp = []

territoriesDict = {}

while tline:
	temp = tline.split(',')
	print(temp)
	tline = territoriesFile.readline()
territoriesFile.close()


while sline:
	temp = sline.split(',')
	print(temp)
	sline = gameStateFile.readline()
gameStateFile.close()

