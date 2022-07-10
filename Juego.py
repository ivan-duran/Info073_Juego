#Integrantes
#Ivan Durán 21.521.054-5
#Ariana Gómez 26.529.225-9
#Eduardo Barrera 21.229.402-0
#José Cáceres 21.205.805-K


import pygame, sys, random
                
# Valida Obstaculos
def valida_potions(x, y, potions_list, potions_hit):
    
    for i in range (len(potions_list)):

        # si colisiona 
        if potions_list[i][0]//30 == x//30 and potions_list[i][1]//30 == y//30:
            potions_hit += 1
            potions_list[i] = (0, 0)
            
            
    return (potions_list, potions_hit)

  
# Valida Obstaculos
def valida_obstacle(x, y, obstacle_list):
    validacion=0
    for i in range (len(obstacle_list)):

        # si colisiona 
        if obstacle_list[i][0]//30 == x//30 and obstacle_list[i][1]//30 == y//30:
            validacion = True

    if validacion:
        return(False)
    else:
        return(True)


# Aparicion Obstaculos y pociones
def spawn(table, dado, pos1, pos2):
    count = 1
    list = []
    while count <= dado:
            for i in range (20):
            
                    for j in range (20):
                        
                        if table[j][i] == pos1 or table[j][i] == pos2:

                            if random.uniform(0, 1) <= 0.1:
                                if count <= dado:
                                    list.append((i*30, j*30))
                                    count += 1
    return(list)
    
# Pociones sobre piedras
def potions_obstacles(potions_list, obstacles_list):
    
    for i in (obstacles_list):
        for j in (potions_list):
            if (i ==j):
                return(True)
    return(False)
            





# Aparicion Jugador y Computadoras
def bot_spawn(table):
    
    count = 0
    while count < 1:
            for i in range (20):
            
                    for j in range (20):
                        
                        if table[j][i] == 1 or table[j][i] == 2:

                            if random.uniform(0, 1) <= 0.001:
                                if count != 1:
                                    bot_x = i * 30
                                    bot_y = j * 30
                                count += 1

    return[bot_x, bot_y]

# Validacion bots sobre roca
def bots_rocas(obstacles_list, bot_x, bot_y):

    for i in (obstacles_list):
        if (i[0]==bot_x or i[1]== bot_y):
            return(True)
    return(False)

# Cosa matar
def cosa_killer(cosa_x, cosa_y, bot_x, bot_y, la_cosa_contador):
    if cosa_x//30 == bot_x//30 and cosa_y//30 == bot_y//30:
            la_cosa_contador += 1
            bot_x = -100
            bot_y = -100
    return(bot_x, bot_y, la_cosa_contador)


# Movimiento de las computadoras
def bot_move(table, bot_x, bot_y, bot_speed, bot_width, obstacle_list):

    loop = True    
    while loop:
        if random.uniform(0, 1) <= 0.5:
            #horizontalmente
            if random.uniform(0, 1) <= 0.5:
                #derecha
                if table[(bot_y)//30] [(bot_x + bot_width) //30]!= 0 and table[(bot_y + bot_width)//30] [(bot_x + bot_width) //30]!= 0 and bot_x + 20 + bot_speed < 600 :      

                            
                    if valida_obstacle(bot_x + bot_width + bot_speed, bot_y , obstacle_list) and valida_obstacle(bot_x + bot_width, bot_y + bot_width, obstacle_list):
                             bot_x += bot_speed
            
            else:
                #Izquierda
                if table[(bot_y)//30] [(bot_x - bot_speed) //30]!= 0 and table[(bot_y + bot_width)//30] [(bot_x - bot_speed) //30]!= 0 and (bot_x - bot_speed) > 0:                                                          
                   

                    if valida_obstacle(bot_x - bot_speed, bot_y, obstacle_list) and valida_obstacle(bot_x - bot_speed, bot_y + bot_width, obstacle_list) :
                            bot_x  -= bot_speed
                    

        else:
            #Verticalmente
            if random.uniform(0, 1) <= 0.5:
                #Arriba
                if table[(bot_y - bot_speed)//30] [(bot_x) //30]!= 0 and table[(bot_y - bot_speed)//30] [(bot_x + bot_width) //30]!= 0 and bot_y - bot_speed > 0:                                                        
                    

                    if valida_obstacle(bot_x, bot_y - bot_speed, obstacle_list) and valida_obstacle(bot_x + bot_width, bot_y - bot_speed, obstacle_list) :
                            bot_y  -= bot_speed                    
            else:
                #Abajo
                if table[(bot_y + bot_width)//30] [(bot_x) //30]!= 0 and table[(bot_y + bot_width)//30] [(bot_x + bot_width) //30]!= 0 and bot_y + 20 + bot_speed < 600:                                                          
                   

                    if valida_obstacle(bot_x , bot_y + bot_width + bot_speed, obstacle_list) and valida_obstacle(bot_x + bot_width, bot_y + bot_width, obstacle_list) :
                             bot_y  += bot_speed
        loop = False





    return [bot_x, bot_y]



            
            
            




#Main Menu
def main_menu():


    screen_WIDTH = 600
    screen_HEIGHT = 600
    screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))


    menu_background = pygame.image.load("menu_background.png")
    pygame.display.set_caption('Slime SUS')
  


    mainClock = pygame.time.Clock()
    pygame.init()
    



    menu=True
    while menu:

          
        screen.blit(menu_background, [0,0])
        pygame.display.update()
        mainClock.tick(60)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                menu=False
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                if event.key == pygame.K_i:
                    instruction()

        pygame.display.update()


# Instrucciones
def instruction():

    screen_WIDTH = 600
    screen_HEIGHT = 600
    screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))


    instrucciones_foto = pygame.image.load("instrucciones.png")
    pygame.display.set_caption('Slime SUS')
  


    mainClock = pygame.time.Clock()
    pygame.init()
    



    si = True
    while si:
        screen.blit(instrucciones_foto, [0,0])
        pygame.display.update()
        mainClock.tick(60)

  

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                si=False
                sys.exit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        si = False
                if event.key == pygame.K_SPACE:
                    main()
        
# Juego en pantalla
def main():
    
    
    pygame.init()
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 10)

    # Ventana y música

    screen_WIDTH = 600
    screen_HEIGHT = 600
    screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

    background = pygame.image.load("background.png")
    win_background = pygame.image.load("win_background.png")
    lose_background = pygame.image.load("lose_background.png")
    

    

    # Tablero: 0 paredes, 1 piezas, 2 Camino
    table = [
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
[0,0,2,2,2,2,2,2,0,0,0,1,1,1,1,1,1,1,0,0],
[1,1,2,0,0,0,0,2,0,0,0,1,1,1,1,1,1,1,0,0],
[1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0],
[1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,2,2,0],
[0,2,2,2,2,2,2,2,1,1,0,0,1,1,1,1,1,0,2,0],
[0,2,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,2,0],
[0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0],
[0,2,0,0,0,0,0,0,2,0,2,0,0,2,0,0,0,0,0,0],
[0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,1,1,1,1,1],
[0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,1],
[2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0],
[2,0,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
[2,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[2,0,1,1,1,0,0,1,2,0,2,2,2,0,1,1,1,1,1,0],
[0,0,0,0,0,0,0,0,2,0,2,0,2,0,1,1,1,1,1,0],
[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]
]
 

 
    # Jugador

    player_font = pygame.font.Font(None, 30)

    player_sprite = pygame.image.load("player.png")
    player_sprite = pygame.transform.scale(player_sprite, (20, 20))
    player_rect = player_sprite.get_rect()
    player_rect.x, player_rect.y  = bot_spawn(table)
    player_speed = 2
    

    # Computadoras

    bot_sprite = pygame.image.load("bot.png")
    bot_sprite = pygame.transform.scale(bot_sprite, (20, 20))
    
    bot_1_rect = bot_sprite.get_rect()
    bot_2_rect = bot_sprite.get_rect()
    bot_3_rect = bot_sprite.get_rect()
    

    bot_1_rect.x, bot_1_rect.y  = bot_spawn(table)
    bot_2_rect.x, bot_2_rect.y = bot_spawn(table)
    bot_3_rect.x, bot_3_rect.y  = bot_spawn(table)

    bot_speed = 10


    # Paredes - Piezas - Camino

    tree = pygame.image.load("Arbol.png")
    tree = pygame.transform.scale(tree, (30, 30))

    room = pygame.image.load("flowers.png")
    room = pygame.transform.scale(room, (30, 30))
    
    road = pygame.image.load("road.png")
    road = pygame.transform.scale(road, (30, 30))
    

    # Pociones 

    potions_font = pygame.font.Font(None, 30) 

    potions_sprite = pygame.image.load("pociones.png")
    potions_sprite = pygame.transform.scale(potions_sprite, (18, 18))

    potions_dado = random.randint(35, 50)
    potions_list = spawn(table, potions_dado, 1, 2)
    potions_hit = 0 

    # Obstaculos
    obstacle_sprite = pygame.image.load("obstaculo.png")
    obstacle_sprite = pygame.transform.scale(obstacle_sprite, (25, 25))

    obstacle_dado = random.randint(10, 15)
    obstacle_list = spawn(table, obstacle_dado, 1, 1)
    
    # ------ Validaciones sobre rocas -------
    while potions_obstacles(potions_list, obstacle_list):
        potions_list = spawn(table, potions_dado, 1, 2)

    while bots_rocas(obstacle_list, bot_1_rect.x, bot_1_rect.y):
        bot_1_rect.x, bot_1_rect.y  = bot_spawn(table)

    while bots_rocas(obstacle_list, bot_2_rect.x, bot_2_rect.y):
        bot_2_rect.x, bot_2_rect.y  = bot_spawn(table)

    while bots_rocas(obstacle_list, bot_3_rect.x, bot_3_rect.y):
        bot_3_rect.x, bot_3_rect.y  = bot_spawn(table)

    while bots_rocas(obstacle_list, player_rect.x, player_rect.y):
        player_rect.x, player_rect.y  = bot_spawn(table)


    # La Cosa
    la_cosa_dado= random.randint(0,3)
    muerte_font = pygame.font.Font(None, 30)
    
    run = True
    bot_count_move = 0 
    la_cosa_contador = 0

    while  run :
        
        screen.blit(background, [0,0])

        clock.tick(60)


       


        # Tablero
        for i in range (20):
    
            for j in range (20):
        
                
                # Paredes
                if table[j][i] == 0:
                    
                    screen.blit(tree, (i*30, j*30))

                
                # Habitaciones
                if table[j][i] == 1:
                    
                    screen.blit(room, (i*30, j*30))
                
                # Camino
                if table[j][i] == 2:
                    
                    screen.blit(road, (i*30, j*30))
        
        # La cosa

        if la_cosa_dado == 0:
            player_text = player_font.render("Eres la cosa",0 ,(0, 0, 0))
            screen.blit(player_text,(80, 0))
            bot_1_rect.x, bot_1_rect.y, la_cosa_contador = cosa_killer(player_rect.x, player_rect.y, bot_1_rect.x, bot_1_rect.y, la_cosa_contador)
            bot_2_rect.x, bot_2_rect.y, la_cosa_contador = cosa_killer(player_rect.x, player_rect.y, bot_2_rect.x, bot_2_rect.y, la_cosa_contador)
            bot_3_rect.x, bot_3_rect.y, la_cosa_contador = cosa_killer(player_rect.x, player_rect.y, bot_3_rect.x, bot_3_rect.y, la_cosa_contador) 
            

        
        elif la_cosa_dado == 1:
            player_rect.x, player_rect.y, la_cosa_contador = cosa_killer(bot_1_rect.x, bot_1_rect.y, player_rect.x, player_rect.y, la_cosa_contador)
            
            bot_2_rect.x, bot_2_rect.y, la_cosa_contador = cosa_killer(bot_1_rect.x, bot_1_rect.y, bot_2_rect.x, bot_2_rect.y, la_cosa_contador)
            bot_3_rect.x, bot_3_rect.y, la_cosa_contador = cosa_killer(bot_1_rect.x, bot_1_rect.y, bot_3_rect.x, bot_3_rect.y, la_cosa_contador)
        elif la_cosa_dado == 2:
            player_rect.x, player_rect.y, la_cosa_contador = cosa_killer(bot_2_rect.x, bot_2_rect.y, player_rect.x, player_rect.y, la_cosa_contador)

            bot_1_rect.x, bot_1_rect.y, la_cosa_contador = cosa_killer(bot_2_rect.x, bot_2_rect.y, bot_1_rect.x, bot_1_rect.y, la_cosa_contador)
            bot_3_rect.x, bot_3_rect.y, la_cosa_contador = cosa_killer(bot_2_rect.x, bot_2_rect.y, bot_3_rect.x, bot_3_rect.y, la_cosa_contador)
        elif la_cosa_dado == 3:
            player_rect.x, player_rect.y, la_cosa_contador = cosa_killer(bot_3_rect.x, bot_3_rect.y, player_rect.x, player_rect.y, la_cosa_contador)

            bot_1_rect.x, bot_1_rect.y, la_cosa_contador = cosa_killer(bot_3_rect.x, bot_3_rect.y, bot_1_rect.x, bot_1_rect.y, la_cosa_contador)
            bot_2_rect.x, bot_2_rect.y, la_cosa_contador = cosa_killer(bot_3_rect.x, bot_3_rect.y, bot_2_rect.x, bot_2_rect.y, la_cosa_contador)

        

            



        # Pociones y Obstaculos
        for i in range(potions_dado):
            screen.blit(potions_sprite, potions_list[i])
        for i in range(obstacle_dado):
            
            screen.blit(obstacle_sprite, obstacle_list[i])

        potions_list, potions_hit = valida_potions(player_rect.x, player_rect.y, potions_list, potions_hit)
        potions_list, potions_hit = valida_potions(bot_1_rect.x, bot_1_rect.y, potions_list, potions_hit)
        potions_list, potions_hit = valida_potions(bot_2_rect.x, bot_2_rect.y, potions_list, potions_hit)
        potions_list, potions_hit = valida_potions(bot_3_rect.x, bot_3_rect.y, potions_list, potions_hit)

        potions_text = (str(potions_hit) + ("/") + str(potions_dado))
        
        potions_count = potions_font.render(potions_text,0 ,(0, 0, 0))

        screen.blit(potions_count,(25, 0))
        
        
        # Eventos       
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    sys.exit()

            # ----- Movimiento Jugador
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_w:                          
                    if table[(player_rect.y - player_speed)//30][player_rect.x//30] != 0 and table[player_rect.y//30][(player_rect.x + player_sprite.get_width() - player_speed) //30] != 0 and player_rect.y - player_speed > 0 :
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x, player_rect.y - player_speed, obstacle_list) and valida_obstacle(player_rect.x + player_sprite.get_width(), player_rect.y - player_speed, obstacle_list) :
                            player_rect.y -= player_speed
                        
                        
                if event.key == pygame.K_a:
                    if table[player_rect.y//30][(player_rect.x - player_speed) //30] != 0 and table[(player_rect.y + player_sprite.get_height() - player_speed)//30][(player_rect.x - player_speed) //30] != 0 and player_rect.x - player_speed > 0 :
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x - player_speed, player_rect.y, obstacle_list) and valida_obstacle(player_rect.x - player_speed, player_rect.y + player_sprite.get_height(), obstacle_list) :
                            player_rect.x -= player_speed

                if event.key == pygame.K_s:
                    if table[(player_rect.y + player_sprite.get_height())//30][(player_rect.x + player_sprite.get_width() - player_speed)//30] != 0 and table[(player_rect.y + player_sprite.get_height())//30][(player_rect.x)//30] != 0 and player_rect.y + player_sprite.get_height() + player_speed < screen_HEIGHT:
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x , player_rect.y + player_sprite.get_height() + player_speed, obstacle_list) and valida_obstacle(player_rect.x + player_sprite.get_width(), player_rect.y + player_sprite.get_height(), obstacle_list) :
                            player_rect.y += player_speed
                       

                if event.key == pygame.K_d:
                    
                    if table[player_rect.y//30][(player_rect.x + player_sprite.get_width())//30] != 0 and table[(player_rect.y + player_sprite.get_height() - player_speed)//30][(player_rect.x + player_sprite.get_width())//30] != 0 and player_rect.x + player_sprite.get_width() + player_speed < screen_WIDTH :
                        
                        #Obstaculos
                        if valida_obstacle(player_rect.x + player_sprite.get_width() + player_speed, player_rect.y , obstacle_list) and valida_obstacle(player_rect.x + player_sprite.get_width(), player_rect.y + player_sprite.get_height(), obstacle_list):
                            player_rect.x += player_speed

                if event.key == pygame.K_r :
                        run = False
                
                    

              
                    
                            
                
    

       
        


        # Movimiento Computadoras

        bot_count_move += 1

        if bot_count_move == 6:
            bot_count_move = 0
            
            bot_1_rect.x, bot_1_rect.y  = bot_move(table, bot_1_rect.x, bot_1_rect.y, bot_speed, bot_sprite.get_width(),obstacle_list)
            bot_2_rect.x, bot_2_rect.y  = bot_move(table, bot_2_rect.x, bot_2_rect.y, bot_speed, bot_sprite.get_width(),obstacle_list)
            bot_3_rect.x, bot_3_rect.y  = bot_move(table, bot_3_rect.x, bot_3_rect.y, bot_speed, bot_sprite.get_width(),obstacle_list)
        
       
        # Pantalla

        screen.blit(player_sprite, player_rect)
        screen.blit(bot_sprite, bot_1_rect)
        screen.blit(bot_sprite, bot_2_rect)
        screen.blit(bot_sprite, bot_3_rect)
        if player_rect.x<0:
            pygame.draw.rect(screen, (105,214,116), (100,0,470,20))
            muerte_text = muerte_font.render("Te mataron, presiona [r] para empezar de nuevo",0 ,(0, 0, 0))
            screen.blit(muerte_text,(100, 0))

       
        if la_cosa_dado == 0:
            if la_cosa_contador == 3:
                #el jugador como cosa gana
                screen.blit(win_background, [0,0])
            if potions_dado == potions_hit:
                #el jugador como cosa pierde
                screen.blit(lose_background, [0,0])
        else:
            if potions_dado == potions_hit:
                #jugador gana 
                screen.blit(win_background, [0,0])
            if la_cosa_contador== 3:
                screen.blit(lose_background, [0,0])
            
            
            

        
        
        
        

            
        pygame.display.flip()

# Soundtrack
pygame.init()
soundtrack = pygame.mixer.Sound("soundtrack.wav") 
soundtrack.play(-1)
soundtrack.set_volume(0.2)

main_menu()


# Referencias:
# El slime azul de la pantalla de instrucciones, derrota y victoria es de el anime  "Tensei Shitara Slime Datta Ken"
# La imagen de la portada es la del juego "Slime Rancher"
# La musica es: Lost Woods. Composers: Koji Kondo. Del juego "The legend of Zelda: Ocarina of time"
