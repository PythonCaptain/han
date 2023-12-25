import pgzrun
import random

WIDTH = 1000
HEIGHT = 800
TITLE = "Game V1.0"
speed_monster = 5

monsterList = ["monster", "monster_2"]
backgroundList = ["red", "Blue", "#77bf3d", ( 173 , 123 , 212 )]
monster = Actor("monster", (500, 400)) 
background = random.choice(backgroundList)


def update():
    global background, speed_monster
    monster.x += speed_monster
    if monster.x >= 1100 :
        monster.x = - 100
        monster.image = random.choice(monsterList)
        background = random.choice(backgroundList)
        # speed_monster += 5

        if speed_monster <= 20 :
            speed_monster += 5

def draw():
    global backgroundList
    # screen.fill("blue") 
    screen.fill("#77bf3d") 
    screen.fill(background) 

    # screen.fill(( 119 , 191 , 61 )) 
    # screen.fill(( 93.23 , 0.52 , 0.49 )) 
    monster.draw()

pgzrun.go()