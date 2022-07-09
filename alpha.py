from tkinter import scrolledtext 
from turtle import width
import pygame, sys, random


#COLORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_WIDTH = 700
screen_HEIGHT = 700
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))

pygame.display.set_caption('La Cosa')

background = pygame.image.load("background.png").convert()

player_image = pygame.image.load("bettercall.jpg").convert()

enemy_image = pygame.image.load("señorblanco.png").convert()




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
    
        self.rect = self.image.get_rect() #Para poder posicionar sprite

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        
        self.rect = self.image.get_rect() #Para poder posicionar sprite

        
        


class Game(object):

    def __init__(self):
        
        self.game_over = False

        self.score = 0
        self.enemy_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        for i in range(3):
            enemy = Enemy()
            enemy.rect.x = random.randrange(screen_WIDTH - enemy_image.get_width())
            enemy.rect.y = random.randrange(screen_HEIGHT - enemy_image.get_height())

            self.enemy_list.add(enemy)
            self.all_sprite_list.add(enemy)

        #Player
        self.player = Player()
        self.player_list.add(self.player)

        self.player.rect.x = random.randrange(screen_WIDTH - player_image.get_width())
        self.player.rect.y = random.randrange(screen_HEIGHT - player_image.get_height())
        
        self.player_speed_x = 0
        self.player_speed_y = 0
        self.all_sprite_list.add(self.player)
        self.contadorMovimiento= 0        
        
    def process_events(self):
        for event in pygame.event.get():
            
            
            #Reiniciar juego
            
            #Mover jugador
            if event.type == pygame.KEYDOWN:

                # player 
                if event.key == pygame.K_w:
                    self.player_speed_y = -3

                if event.key == pygame.K_a:
                    self.player_speed_x = -3

                if event.key == pygame.K_s:
                    self.player_speed_y = 3

                if event.key == pygame.K_d:
                    self.player_speed_x = 3

            if event.type == pygame.QUIT:
                return True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.game_over:
                        self.__init__()

        

            if event.type == pygame.KEYUP:  

                # player 
                if event.key == pygame.K_w:
                    self.player_speed_y = 0

                if event.key == pygame.K_a:
                    self.player_speed_x = 0

                if event.key == pygame.K_s:
                    self.player_speed_y = 0

                if event.key == pygame.K_d:
                    self.player_speed_x = 0
        return False

    def run_logic(self):
        
        if not self.game_over:
            enemy_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True) #eliminar sprite al pasar encima

            pygame.sprite.spritecollide(self.player, self.enemy_list, True)
            
            for enemy in enemy_hit_list:
                self.score += 1
                print(self.score)

            self.player.rect.x += self.player_speed_x
            self.player.rect.y += self.player_speed_y

            if (self.player.rect.x + player_image.get_width() >= screen_WIDTH or  self.player.rect.x <= 0):
                self.player_speed_x = 0

            if (self.player.rect.y + player_image.get_height() >= screen_HEIGHT or self.player.rect.y <= 0):
                self.player_speed_y = 0

            

            #Movimiento enemigos
            self.contadorMovimiento += 1
            if self.contadorMovimiento == 10:
                self.contadorMovimiento = 0
                for enemy in self.enemy_list:
                    if enemy.rect.x <= 650 and enemy.rect.x >= 50 and enemy.rect.y >= 50 and enemy.rect.y <= 650: 
                        if random.uniform(0, 1) <= 0.5:
                            #horizontalmente
                            if random.uniform(0, 1) <= 0.5:
                                #derecha
                                enemy.rect.x += 20
                            else:
                                #Izquierda
                                enemy.rect.x  -= 20
                        else:
                            #Verticalmente
                            if random.uniform(0, 1) <= 0.5:
                                #Arriba
                                enemy.rect.y -= 20
                            else:
                                #Abajo
                                enemy.rect.y += 20
                    else:
                        if enemy.rect.x > 600 or enemy.rect.y > 600:
                            enemy.rect.x -= 20
                            enemy.rect.y -= 20
                        else:
                            enemy.rect.x += 50
                            enemy.rect.y += 50

            
            if len(self.enemy_list) == 0:
                self.game_over = True
            elif len(self.player_list) == 0:
                self.game_over = True

    def display_frame(self, screen):
        
        screen.fill((255, 255, 255))

        screen.blit(background, [0,0])

        

        if self.game_over:
            print("Game_over")
        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render('Preciona "R" para reiniciar', True, BLACK)
            center_x = (screen_WIDTH // 2) - (text.get_width() // 2)
            center_y = (screen_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
        if not self.game_over:
            self.all_sprite_list.draw(screen)
        pygame.display.flip()

def main():
    pygame.init()

    screen = pygame.display.set_mode([screen_WIDTH,screen_HEIGHT])

    done = False
    clock = pygame.time.Clock()

    game = Game()

    soundtrack = pygame.mixer.Sound("soundtrack.wav")
    soundtrack.play(-1)
    soundtrack.set_volume(0.1)

    
    
    while not done:
        done = game.process_events()

        game.run_logic()
        
        game.display_frame(screen)

        clock.tick(60)

if __name__ == "__main__":
    
    main()























