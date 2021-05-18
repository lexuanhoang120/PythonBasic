import pygame as pg
import random as rnd
import time


pg.init()
width,columns,rows=400,15,30
distance=width//columns
height=distance*rows

#load image
picture=[]
for n in range(8):
    picture.append(pg.transform.scale(pg.image.load(f"T_{n}.jpg"),(distance,distance)))



screen=pg.display.set_mode([width,height])
pg.display.set_caption("Tetris Game")

grid[19]=2

status=True
while status:
    for event in pg.event.get():
        if event.type=pg.QUIT:
            status=False

    screen.fill(128,128,128)
    for n,color in enumerate(grid):
        if color>0:
            x=n%columns*distance
            y=n//columns*distance
            screen.blit(picture[])




pg.quit()
