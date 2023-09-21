
from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('Circle')

    # 일단 그림을 그리자
    cx, cy, r = 400, 300, 200
    for degree in range(0,360,1):
        x = cx + r * math.cos(math.radians(degree))
        y = cy + r * math.sin(math.radians(degree))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)

def run_rectangle():
    print('Rectangle')

    for x in range(50,750 + 1,10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        delay(0.01)




    
    pass



while True:
    #run_circle()
    run_rectangle()
   # run_circle()
    break



close_canvas()
