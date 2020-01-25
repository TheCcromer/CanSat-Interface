#librerias que se importan
import pygame 
import time


#inicializa todos los modulos de pygame
#retorna si la inicializacion fue exitosa o no 
pygame.init()

#va a ser nuestra superficie 
display = pygame.display.set_mode((1298,768)) #Resolucion de la ventana

pygame.display.set_caption('CanSat') #titulo de la ventana 


myColor = (10,26,56) #fondo
orange = (255,127,80) #botones
white = (255,255,255) #color de letra 

#variable necesaria para los textos
font = pygame.font.SysFont(None,25)

#Estilo de los textos
def textObjects(text,color):
	textSurface = font.render(text,True,color)
	return textSurface, textSurface.get_rect()

#texto de los botones
def textToButton(msg,color,buttonx,buttony,buttonwidth,buttonheight):
	textSurf, textRect = textObjects(msg,color)
	textRect.center = ((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
	display.blit(textSurf,textRect)
	
#funcion que lee si se le hizo click al boton 
def button(msg,x,y,width,height):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x + width > cur[0] > x and y + height > cur[1] > y and click[0] == 1:
		buttonActions(msg)
		
#Acciones de los diferentes botones, cada uno lleva a la funcion definida
def buttonActions(msg):
	if msg == "Exit":
		pygame.quit()
		quit()
	if msg == "Tempeture":
		print(msg)
	if msg == "Pressure":
		print(msg)
	if msg == "Voltage":
		print(msg)
	if msg == "Air speed":
		print(msg)
	if msg == "Altitude":
		print(msg)
	if msg == "General":
		general()
	if msg == "Trajectory":
		print(msg)
	if msg == "Return":
		init()
		


#metodo de inicializacion 
def init():

	display.fill(myColor)
	
	image = pygame.image.load(r'logo.jpeg')
	image = pygame.transform.scale(image, (420, 320))
	display.blit(image,(439,125))
	
	#Uso de draw  eje x, eje y, largo, altura
	
	#izquierda
	pygame.draw.rect(display,orange, (100,125,200,75))
	pygame.draw.rect(display,orange, (100,320,200,75))
	pygame.draw.rect(display,orange, (100,515,200,75))

	#derecha
	pygame.draw.rect(display,orange, (1000,125,200,75))
	pygame.draw.rect(display,orange, (1000,320,200,75))
	pygame.draw.rect(display,orange, (1000,515,200,75))
	
	#Centro
	pygame.draw.rect(display,orange, (550,515,200,75))
	
	#Exit
	pygame.draw.rect(display,myColor, (1100,625,200,75))
	
	#codigo para poner el texto en los rectangulos
	textToButton("Voltage",white,100,125,200,75)
	textToButton("Air speed",white,100,320,200,75)
	textToButton("Altitude",white,100,515,200,75)
	textToButton("Trajectory",white,1000,125,200,75)
	textToButton("Tempeture",white,1000,320,200,75)
	textToButton("Pressure",white,1000,515,200,75)
	textToButton("General",white,550,515,200,75)
	textToButton("Exit",white,1100,625,200,75)

	#Aplica los cambios realizados en el fondo
	pygame.display.update()
	
	time.sleep(1)
	
	mainloop = True

	while mainloop:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
	
		#espera de los evento de presionar los botones 
		button("Voltage",100,125,200,75)
		button("Air speed",100,320,200,75)
		button("Altitude",100,515,200,75)
		button("Trajectory",1000,125,200,75)
		button("Tempeture",1000,320,200,75)
		button("Pressure",1000,515,200,75)
		button("General",550,515,200,75)
		button("Exit",1100,625,200,75)
		
#Inicializa el fondo y aplica los valores para mostrar la ventana general	
def general():
	display.fill(myColor)
	
	#Return
	pygame.draw.rect(display,myColor, (1100,625,200,75))
	textToButton("Return",white,1100,625,200,75)
	
	#Aplicar los cambios en el fondo
	pygame.display.update()
	
	
	mainloop = True
	#este while es el mainloop
	while mainloop:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainloop = False
		
		button("Return",1100,625,200,75)
	
#llama a la funcion que inicializa todo el programa 	
init()
