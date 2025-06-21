import pygame
import sys
import garden
from garden import GardenManager
from game_utils import GameTimer, draw_background, run_game
from seed import Seed

WIDTH, HEIGHT = 800, 600



def student_defense(garden_manager, timer):
    # Make all plants grow twice as fast
    garden_manager.set_growth_rate(2)
    garden_manager.set_max_plant_height(200)
    # Plant a new seed every 5 seconds
    if timer % (60 * 2) == 0:
        garden_manager.plant_seed()

    # Use bug spray if there are more than 2 bugs
    #if len(garden_manager.pests) > 2:
     #   garden_manager.bug_spray()

    # Freeze all bugs for 2 seconds every 20 seconds
    #if timer % (60 * 20) == 0:
    #    garden_manager.freeze_bugs(frames=120)



if __name__ == "__main__":
    run_game(student_defense)
