import time
import random
from adafruit_circuitplayground.express import cpx

GREEN_LIGHT = True
GAME_OVER = False
ENG_GAME_SOUND_EFFECT_PLAYED = False
INTERVAL_SET = False
GREEN_LIGHT_CYCLE_SET = False

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
        if GREEN_LIGHT_CYCLE_SET == False:
            target_green_light_cyle_index = random.randrange(0, 2)
            green_light_cyle_index = 0
            GREEN_LIGHT_CYCLE_SET = True

        turn_on_lights((0, 255, 0))
        cpx.play_file("green-light.wav")
        turn_on_lights((0, 0, 0))
        basline_xyz = cpx.acceleration
        # red light
        if green_light_cyle_index == target_green_light_cyle_index:
            time_green_light_stopped = time.monotonic()
            GREEN_LIGHT_CYCLE_SET = False
            GREEN_LIGHT = False
            continue

        green_light_cyle_index += 1
    else:
        time.sleep(.1)
        
        if GAME_OVER:
            turn_on_lights((255, 0, 0))
            time.sleep(.9)
            turn_on_lights((0, 0, 0))

            if ENG_GAME_SOUND_EFFECT_PLAYED == False:
                cpx.play_file("game-over.wav") 
                ENG_GAME_SOUND_EFFECT_PLAYED = True

            # reset the game
            if cpx.button_a or cpx.button_b:
                GREEN_LIGHT = True
                GAME_OVER = False
                ENG_GAME_SOUND_EFFECT_PLAYED = False
                print("Button pressed!")
        else:
            # read for current movement, end game if user moved
            current_xyz= cpx.acceleration
            if player_moved(basline_xyz, current_xyz):
                GAME_OVER = True


            # set green light if random amount of time has passed
            now = time.monotonic()
            if INTERVAL_SET == False:
                random_interval = random.randrange(2, 11)
                INTERVAL_SET = True
                
            if now - time_green_light_stopped > random_interval:
                INTERVAL_SET = False
                GREEN_LIGHT = True