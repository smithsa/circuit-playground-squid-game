import time
import random
from adafruit_circuitplayground.express import cpx

GREEN_LIGHT = True
GAME_OVER = False
ENG_GAME_SOUND_EFFECT_PLAYED = False

def turn_on_lights(color):
    for i in range(len(cpx.pixels)):
        cpx.pixels[i] = color

def player_moved(basline_xyz, current_xyz):
    for i in range(len(basline_xyz)):
        min_xyz = round(basline_xyz[i] - 1)
        max_xyz = round(basline_xyz[i] + 2)
        xyz_range = range(min_xyz, max_xyz)
        cur_input = round(current_xyz[i])

        if(cur_input in xyz_range):
            return False

    return True        

while True:
    if GREEN_LIGHT:
        # TODO - can this be played on a loop
        turn_on_lights((0, 255, 0))
        cpx.play_file("green-light.wav")
        turn_on_lights((0, 0, 0))
        baseline_x, baseline_y, baseline_z = cpx.acceleration
        basline_xyz = (baseline_x, baseline_y, baseline_z)
        GREEN_LIGHT = False
        time_green_light_stopped = time.monotonic()
    else:
        time.sleep(.1)
        
        if GAME_OVER:
            if(ENG_GAME_SOUND_EFFECT_PLAYED == False):
                cpx.play_file("game_over.wav") 
                ENG_GAME_SOUND_EFFECT_PLAYED = True
            
            turn_on_lights((255, 0, 0))
            time.sleep(.9)
            turn_on_lights((0, 0, 0))

            # reset the game
            if cpx.button_a or cpx.button_b:
                GREEN_LIGHT = True
                GAME_OVER = False
                ENG_GAME_SOUND_EFFECT_PLAYED = False
                print("Button pressed!")
        else:
            # read for current movement, end game if user moved
            current_x, current_y, current_z = cpx.acceleration
            current_xyz = (current_x, current_y, current_z)
            if(player_moved(basline_xyz, current_xyz)):
                GAME_OVER = True


            # set green light if random amount of time has passed
            now = time.monotonic()
            if now - time_green_light_stopped > random.randrange(2, 11):
                GREEN_LIGHT = True