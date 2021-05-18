import pgzrun
from  random import randint

WIDTH = 534
HEIGHT = 534
score = 0
game_over = False
mario = Actor("mario")
mario.pos = 100, 200
coin = Actor("coin")
coin.pos = 300, 300
music.play("nhac")

def draw():
    screen.blit("background", (0, 0))
    mario.draw()
    coin.draw()
    screen.draw.text("Score "+str(score),color="black",topleft=(10,10))
    if game_over:
        screen.blit("background", (0, 0))
        screen.draw.text("Final score "+str(score),color="black",topleft=(10,10))

def play_coin():
    coin.x=randint(20,(WIDTH-20))
    coin.y=randint(20,(HEIGHT-20))

def update():
    global score
    if keyboard.left:
        mario.x=mario.x-4
    elif keyboard.right:
        mario.x=mario.x+4
    elif keyboard.up:
        mario.y=mario.y-4
    elif keyboard.down:
        mario.y=mario.y+4
    coin_collected=mario.colliderect(coin)
    if coin_collected:
        score=score+10
        play_coin()

def time_up():
    global game_over
    game_over=True
clock.schedule(time_up,10.0)


play_coin()

pgzrun.go()
