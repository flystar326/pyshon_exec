import itertools, sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *

def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0: #��
        velocity.y = -vel
    elif direction == 2: #��
        velocity.x = vel
    elif direction == 4: #��
        velocity.y = vel
    elif direction == 6: #��
        velocity.x = -vel
    return velocity

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("��ƻ��")
font = pygame.font.Font(None, 36)
timer = pygame.time.Clock()

#����������
player_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

#��ʼ����Ҿ�����
player = MySprite()
player.load("farmer walk.png", 96, 96, 8)
player.position = 80, 80
player.direction = 4
player_group.add(player)

#��ʼ��food������

for n in range(1,50):
    food = MySprite();
    food.load("food_low.png", 35, 35, 1)
    food.position = random.randint(0,780),random.randint(0,580)
    food_group.add(food)

game_over = False
player_moving = False
player_health = 0


while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    else:
        player_moving = False


    if not game_over:
        #���ݽ�ɫ�Ĳ�ͬ����ʹ�ò�ͬ�Ķ���֡
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns-1
        if player.frame < player.first_frame:
            player.frame = player.first_frame

        if not player_moving:
            #��ֹͣ������������ֹͣ�ƶ���ʱ�򣩣�ֹͣ���¶���֡
            player.frame = player.first_frame = player.last_frame
        else: 
            player.velocity = calc_velocity(player.direction, 1.5)
            player.velocity.x *= 1.5
            player.velocity.y *= 1.5

        #������Ҿ�����
        player_group.update(ticks, 50)

        #�ƶ����
        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0: player.X = 0
            elif player.X > 700: player.X = 700
            if player.Y < 0: player.Y = 0
            elif player.Y > 500: player.Y = 500

        #�������Ƿ���ʳ���ͻ���Ƿ�Ե���ʵ
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, food_group)
        if attacker != None:
            if pygame.sprite.collide_circle_ratio(0.65)(player,attacker):
                player_health +=2;
                food_group.remove(attacker);
        if player_health > 100: player_health = 100
        #����ʳ�ﾫ����
        food_group.update(ticks, 50)

        if len(food_group) == 0:
            game_over = True
    #����
    screen.fill((50,50,100))

    #���ƾ���
    food_group.draw(screen)
    player_group.draw(screen)

    #�������Ѫ����
    pygame.draw.rect(screen, (50,150,50,180), Rect(300,570,player_health*2,25))
    pygame.draw.rect(screen, (100,200,100,180), Rect(300,570,200,25), 2)

    if game_over:
        print_text(font, 300, 100, "G A M E   O V E R")
    
    pygame.display.update()