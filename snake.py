import pygame
import random
import time

pygame.init()                                                   

white = (255, 255, 255) 
green = (0,255,0)
red = (255, 0, 0)                                                 
black = (0, 0, 0)
 
screen_width = 800
screen_height = 670
work_screen_height = 600
 
surface = pygame.display.set_mode((screen_width, screen_height)) # Инициализировать окно или экран для отображения
pygame.display.set_caption('Змейка')                             # Заголовок текущего окна
 
clock = pygame.time.Clock()
 
snake_block = 20
speed = 15

 
def upd_snake(snake_block, snake_list):
    for xs in snake_list:
        pygame.draw.rect(surface, green, [xs[0], xs[1], snake_block, snake_block]) 



def game_func():  

    game_over = False
    game_close = False
 
    # Змейка
    x = screen_width / 2 
    y = work_screen_height / 2 

    # Еда
    food_x = round(random.randrange(0,screen_width  - 20) / 20.0) * 20.0
    food_y = round(random.randrange(0,work_screen_height - 20) / 20.0) * 20.0

    # Переменные для сохранения обновленных координат
    x_new = 0                                                  
    y_new = 0    
 
    # Длина змейки
    snake_list = []
    snake_Length = 1
    
    # Направление змейки
    direction = 'not'

    while not game_over:
 
        while game_close == True:
            surface.fill(black)
            letter_size = 50 # размер букв
            name = None      # имя шрифта
            font_style = pygame.font.SysFont(name, letter_size)
            message = font_style.render('Вы проиграли', True, green)     

            surface_rect = surface.get_rect()                           
            surface_rect = message.get_rect(center=surface_rect.center)  

            surface.blit(message, surface_rect)                          
            pygame.display.update()


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:                          # выход
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_func()                                      # рестарт
        
        # Управление
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                    x_new = -snake_block
                    y_new = 0
                    direction = "left"
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d)  and direction != "left":
                   x_new = snake_block
                   y_new = 0
                   direction = "right"
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                    x_new = 0
                    y_new = -snake_block
                    direction = "up"
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                    x_new = 0
                    y_new = snake_block
                    direction = "down"
                elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                elif event.key == pygame.K_r:
                        game_func()                                     

        # Змейка коснулась границы => Конец игры
        if x >= screen_width or x < 0 or y >= work_screen_height or y < 0:
            game_close = True

        x += x_new
        y += y_new
        surface.fill(black)  

        # Обновление еды на экране
        pygame.draw.rect(surface, red, [food_x, food_y, snake_block, snake_block])  

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_Length:
            del snake_list[0]
            
        # Змейка сталкивается сама с собой
        for xs in snake_list[:-1]:
            if xs == snake_head:    
                game_close = True
 
        upd_snake(snake_block, snake_list)

        # Cчет
        pygame.draw.rect(surface, white,(0, work_screen_height, screen_width, 20))
        score_font = pygame.font.SysFont(None, 35)
        value = score_font.render("Счет: " + str(snake_Length - 1) , True, green)
        surface.blit(value, [10, screen_height-40])

           
                                                       
        pygame.display.update()

        # Обновление координат еды => увеличение длины змейки
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, work_screen_height - snake_block) / 20.0) * 20.0
            snake_Length += 1
      
        # ограничение fps
        clock.tick(speed)                                                           
 
    pygame.quit()
    quit()                                                                         
game_func()