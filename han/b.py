import pgzrun
import os
import random
os.environ["SDL_VIDEO_CENTERED"] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = "game"
monsterList = ['monster', 'monster_2']
colorList = ['white', '#da3b3b', ( 68 , 220 , 220 ), ( 62.08 , 0.87 , 0.67 )]
monster = Actor('monster', (500,350))
background = random.choice(colorList)
speed = 5

def update():
    global background, speed
    monster.x += speed
    if monster.x >= 1100 :
        monster.x = -150
        monster.image = random.choice(monsterList)
        background = random.choice(colorList)
        speed += 5
        if speed >= 50 :
            speed = 5
def draw():
    global background
    screen.fill(background)
    monster.draw()
    

pgzrun.go()