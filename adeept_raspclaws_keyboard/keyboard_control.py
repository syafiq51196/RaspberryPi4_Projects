import pygame

def init():
	pygame.init()
	win = pygame.display.set_mode((500,500)) # create a window
	
def getKey(keyName):
	ans = False
	for ev in pygame.event.get():pass
	# pygame.key.get_pressed # get the state of all keyboard buttons
	keyInput = pygame.key.get_pressed()
	
	myKey = getattr(pygame, 'K_{}'.format(keyName))
	if keyInput [myKey]:
		ans = True
	pygame.display.update()
	
	return ans
	
def main():
	if getKey('F1'):
		print('Key F1 was pressed')
	if getKey('F1') and getKey('UP'):
		print('Key F1 and up arrow was pressed')
	if getKey('F1') and getKey('DOWN'):
		print('Key F1 and down arrow was pressed')
	if getKey('F1') and getKey('RIGHT'):
		print('Key F1 and right arrow was pressed')
	if getKey('F1') and getKey('LEFT'):
		print('Key F1 and left arrow was pressed') 
	
	if getKey('F2'):
		print('Key F2 was pressed')	
	if getKey('F2') and getKey('UP'):
		print('Key F2 and up arrow was pressed')
	if getKey('F2') and getKey('DOWN'):
		print('Key F2 and down arrow was pressed')
	if getKey('F2') and getKey('RIGHT'):
		print('Key F2 and right arrow was pressed')
	if getKey('F2') and getKey('LEFT'):
		print('Key F2 and left arrow was pressed') 
	
	if getKey('F3'):
		print('Key F3 was pressed')
	if getKey('F3') and getKey('UP'):
		print('Key F3 and up arrow was pressed')
	if getKey('F3') and getKey('DOWN'):
		print('Key F3 and down arrow was pressed')
	if getKey('F3') and getKey('RIGHT'):
		print('Key F3 and right arrow was pressed')
	if getKey('F3') and getKey('LEFT'):
		print('Key F3 and left arrow was pressed') 
	
	if getKey('F4'):
		print('Key F4 was pressed')
	
	if getKey('F5'):
		print('Key F5 was pressed')
	
	if getKey('F6'):
		print('Key F6 was pressed')	
	
	if getKey('UP'):
		print('up arrow was pressed')
	if getKey('DOWN'):
		print('down arrow was pressed')	
	if getKey('RIGHT'):
		print('right arrow was pressed')
	if getKey('LEFT'):
		print('left arrow was pressed')


if __name__=='__main__':
	init()
	while True:
		main()