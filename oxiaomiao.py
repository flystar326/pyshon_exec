import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("amiaoaichiyu!")

font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 18)
font3 = pygame.font.Font(None, 34)
pygame.mouse.set_visible(False)

white = 255,255,255
red = 220, 50, 50
yellow = 230,230,50
black = 0,0,0
cat = pygame.image.load("aodamiao_2.png")
width,height = cat.get_size()
pic = pygame.transform.scale(cat, (width, height))
fish = pygame.image.load("fish.png")
width, height = fish.get_size()
fish = pygame.transform.smoothscale(fish, (width//3,height//3))
init = pygame.image.load("init.png")
lives = 10
score = 0
clock_start = 0
game_over = 1
mouse_x = mouse_y = 0
Round = 1
mine = 0
mine_png = pygame.image.load("mine.png")
cat2 = pygame.image.load("aodamiao_3.png")
flag = 0

pos_x = 300
pos_y = 410 - 40

bomb_x = random.randint(0, 500)
mine_x = random.randint(0, 500)
bomb_y = -50
vel_y = 0.4
vel_yy = 0.6
mine_y = -100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == MOUSEMOTION:
            mouse_x,mouse_y = event.pos
            move_x,move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 10
                score = 0
                Round = 1
                vel_y = 0.4
                mine = 0
                flag = 0
                pic = cat
                bomb_y = -50
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    
    screen.fill((0,0,100))
    
    if game_over:
        screen.blit(init, (60, 60))
        print_text(font3, 200, 400, "Clicked To Play!")
        print_text(font2, 310, 480, "adfasdfasdf")
    else:
        if score > 300 and score < 600:
            Round = 2
        elif score > 600 and score < 900:
            Round = 3
        elif score > 900 and score < 1200:
            Round = 4
        elif score > 1200 and score < 1500:
            Round = 5
        elif score >= 1500:
            Round = 6
        
        print_text(font1, 280, 0, "Round: " + str(Round))
        
        if Round == 1:
            vel_y = 0.4
        elif Round == 2:
            vel_y = 0.6
        elif Round == 3:
            vel_y = 0.8
        elif Round == 4:
            vel_y = 1.0
        elif Round == 5:
            vel_y = 1.2
    
        bomb_y += vel_y
        mine_y += vel_yy
    
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
        elif bomb_y > pos_y:
            if bomb_x > pisx-10 and bomb_x < pos_x + 70:
                score += 10
                bomb_x =random.randint(0,500)
                bomb_y = -50
        if Round > 2:
            if mine_y > 500:
                mine_x = random.randint(0, 500)
                mine_y = -50
            elif mine_y > pos_y:
                if mine_x > pos_x and mine_x < pos_x + 40:
                    mine_x = random.randint(0, 500)
                    mine_y = -50
                    lives -= 1
                    pic = cat2
                    if lives == 0:
                        game_over = True
        
        screen.blit(fish, (bomb_x, int(bomb_y)))
        
        if Round > 2:
            screen.blit(mine_png, (mine_x, int(mine_y)))
        
        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 510:
            pos_x = 500
        
        if lives < 5:
            pic = cat2
        
        screen.blit(pic, (pos_x, pos_y))
    
    print_text(font1, 0, 0, "LIVES: ")
    
