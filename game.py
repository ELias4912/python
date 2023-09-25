import pygame as pg 

pg.init()

BLACK  = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

screen =pg.display.set_mode((800,600))

clock = pg.time.Clock()
i = 0
pos_x = 100
pos_y = 100

size_x = 50
size_y = 50

playing  = True
while playing:
    clock.tick(120)

    i += 1

    for event in pg.event.get():
        if event.type == pg.QUIT: 
           playing = False
           pg.quit()

    keys = pg.key.get_pressed()
    if keys [pg.K_w]:
        pos_y -= 5
    if keys [pg.K_s]:
        pos_y += 5
    if keys [pg.K_a]:
        pos_x -= 5
    if keys [pg.K_d]:
        pos_x += 5    

    screen.fill(GREEN)
    player_box = pg.Rect(pos_x,pos_y, 100,100)
    pg.draw.rect(screen, RED, player_box)
    
    if pos_x >  800-size_x:
        pos_x = 800-size_y


       

    

    pg.display.update()