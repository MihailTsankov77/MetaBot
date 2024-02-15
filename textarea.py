import pygame, sys
from pygame.locals import QUIT

pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Ariel',25,False,False)

userText = "hello"
input_rect = pygame.Rect(100,100,100,30)
cursor = 0
active = True 
while True:
	try:
		surface.fill(userText)
	except:
		surface.fill('grey')
	if active:
		boxColor = 'white'
	else:
		boxColor = 'grey'
	textBox = pygame.draw.rect(surface, boxColor, input_rect)
	if cursor%4 == 0 and active:
		userText = userText + "|"
	cursor +=1
		
	textSurface = font.render(userText,True,'black')
	try:
		if userText[-1] == "|":
			userText = userText[:-1]
	except:
		pass
	surface.blit(textSurface,(input_rect.x+5, input_rect.y+5))
	
	input_rect.w = max(100, textSurface.get_width()+15)
	
	for event in pygame.event.get():
		if event.type == QUIT:
				pygame.quit()
				sys.exit()
		elif event.type == pygame.KEYDOWN:
			print(event.unicode, event.unicode.isalpha())
			if event.unicode.isalpha() and active:
				userText = userText + event.unicode
			if (event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE) and active:
				userText = userText[:-1]
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if input_rect.collidepoint(event.pos):
				active = True
			else:
				active = False
	pygame.display.update()
	clock.tick(60)