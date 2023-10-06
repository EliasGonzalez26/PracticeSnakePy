import pygame
import time
import random

snake_speed = 15

#tamaño de pantalla
window_x = 720
window_y = 480

#definiendo colores
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#iniciando pygame
pygame.init()

#iniciando ventana de juego
pygame.display.set_caption('PYSnakes')
game_window = pygame.display.set_mode((window_x, window_y))

#controlador de fps
fps = pygame.time.Clock()

#definiendo posicion de serpiente
snake_position = [100, 50]

#definiendo bloques de cuerpo de serpiente
snake_body=[[100,50],[90,50],[80,50],[70,50]]

#posicion fruta
fruit_position= [random.randrange(1, (window_x//10))*10, random.randrange(1, (window_y//10))*10]
fruit_spawn= True

#seteando direction de serpiente
#derecha
direction= 'RIGHT'
change_to= direction

#puntos iniciales
score = 0

#funcion de despliegue de puntos
def show_score(choice, color, font, size):
    
    #creando font
    score_font = pygame.font.SysFont(font, size)
    
    #creando despliegue de objeto en superficie
    #score_superface
    score_superface = score_font.render('Score :  ' + str(score), True, color)
    
    #creando objeto rectangular para el texto
    #objeto en superficie
    score_rect = score_superface.get_rect()
    
    #desplegando texto
    game_window.blit(score_superface, score_rect)
    
#funcion game over
def game_over():
    #creando objeto de font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    #creando texto en superficie
    game_over_superface = my_font.render(
        'Your Score is :  ' + str(score), True, red)
    
    #creando rectangulo para el texto
    game_over_rect = game_over_superface.get_rect()
    
    #seteando posicion de texto
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    #blit traera el texto a pantalla
    game_window.blit(game_over_superface, game_over_rect)
    pygame.display.flip()
    
    #despues de 2 segundos se borra el progreso
    time.sleep(2)
    
    #desactivar libreria
    pygame.quit()
    
    #salir del programa
    quit()
    
#funcion principal 
while True: 
    
    #manejo de eventos clave
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    
    #si dos teclas se presionan a la vez
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    #movviendo la serpiente
    if direction == 'UP':
        snake_position[1] -=10
    if direction == 'DOWN':
        snake_position[1] +=10
    if direction == 'LEFT':
        snake_position[0] -=10
    if direction == 'RIGHT':
        snake_position[0] +=10
        
    
    #mecanismo de crecimiento de serpiente
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score +=10
        fruit_spawn= False
    else: 
        snake_body.pop()
    
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10))*10, random.randrange(1, (window_y//10))*10]
    
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10,10))
    
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10,10))
    
    #game over Condiciones
    if snake_position[0] < 0 or snake_position[0]>window_x -10:
        game_over()
    if snake_position[1] < 0 or snake_position[1]>window_y -10:
        game_over()
    
    #tocando cuerpo de serpiente
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    #desplegando puntuacion continuamente
    show_score(1, white, 'times new roman', 20)
    
    #refrescar pantalla de juego
    pygame.display.update()
    
    #fps
    fps.tick(snake_speed)



