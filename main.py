import pygame
import sys
from garden import GardenManager
from game_utils import GameTimer, draw_background, run_game


def play_area(garden_manager, timer):
    """
    Students: Write your own code here to protect the plants!
    You can access and modify garden_manager.seeds, garden_manager.pests, etc.
    Example: Remove pests, add shields, etc.
    """
    
    # Example: Remove all pests (uncomment to test)
    # garden_manager.pests.clear()
    pass


if __name__ == "__main__":
    run_game(play_area)
