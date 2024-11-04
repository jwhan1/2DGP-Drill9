from pico2d import *
import random


from Boy import Boy
from Grass import Grass
from Game_world import Game_world

running = True

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False
        elif event.key == SDLK_LEFT or event.key == SDLK_RIGHT or event.key == SDLK_KP_ENTER or SDLK_SPACE:
                boy.handle_event(event)

def reset_world():
    global running
    global boy
    global game_world

    game_world = Game_world()

    boy = Boy()
    game_world.add_object(boy, 1)
    
    grass1 = Grass(0)
    game_world.add_object(grass1, 0)#뒷배경
    grass2 = Grass(1)
    game_world.add_object(grass2, 1)


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()

while running:
    handle_events()
    game_world.update()
    render_world()
    delay(0.016)

close_canvas()
