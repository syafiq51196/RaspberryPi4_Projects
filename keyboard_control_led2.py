import pygame
import time
from led_basic import LED

led= LED()

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

i = 0
j = 0
k = 0
minn = 0
maxn = 255

print(i,j,k)

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def main():
    global i 
    global j 
    global k 
    global minn
    global maxn   
    
    while getKey('F1'):
        print('Key F1 was pressed')
        
        if getKey('LEFT'):
            i -= 1
            print(clamp(i, minn, maxn), j, k)
            led.colorWipe(clamp(i, minn, maxn), j, k)
                    
        if getKey('RIGHT'):
            i += 1
            print(clamp(i, minn, maxn), j, k)
            led.colorWipe(clamp(i, minn, maxn), j, k)
            
    while getKey('F2'):
        print('Key F2 was pressed')
        
        if getKey('LEFT'):
            j -= 1
            print(i, clamp(j, minn, maxn), k)
            led.colorWipe(i, clamp(j, minn, maxn), k)
                        
        if getKey('RIGHT'):
            j += 1
            print(i, clamp(j, minn, maxn), k)
            led.colorWipe(i, clamp(j, minn, maxn), k)
            
    while getKey('F3'):
        print('Key F3 was pressed')
        
        if getKey('LEFT'):
            k -= 1
            print(i, j, clamp(k, minn, maxn))
            led.colorWipe(i, j, clamp(k, minn, maxn))
                    
        if getKey('RIGHT'):
            k += 1
            print(i, j, clamp(k, minn, maxn))
            led.colorWipe(i, j, clamp(k, minn, maxn))
            
if __name__=='__main__':
	init()
	while True:
		main()