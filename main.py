import pygame
import sys
from garden import GardenManager
from game_utils import GameTimer, draw_background, run_game

second = 60

def play_area(garden_manager, timer):
    """
    Students: Write your own code here to protect the plants!
    You can access and modify garden_manager.seeds, garden_manager.pests, etc.
    Example: Remove pests, add shields, etc.
    """
    
    # Example: Remove all pests (uncomment to test)
    # garden_manager.pests.clear()
    if timer % (second * 0.5) == 0:
            garden_manager.plant_seed()
    if timer % (second * 5) == 0:
            garden_manager.freeze_plants()

    if timer % (second * 10) == 0:
            garden_manager.unfreeze_plants()


    pass


if __name__ == "__main__":
    run_game(play_area)
