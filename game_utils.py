import pygame
import sys
import time
from garden import GardenManager
from seed import Seed

WIDTH, HEIGHT = 800, 600

class GameTimer:
    def __init__(self, total_seconds):
        self.total_seconds = total_seconds
        self.start_time = time.time()

    def time_left(self):
        elapsed = int(time.time() - self.start_time)
        return max(0, self.total_seconds - elapsed)

    def is_time_up(self):
        return self.time_left() <= 0

    def get_time(self):
        """Return the time left in seconds."""
        return self.time_left()

def draw_background(screen, width, height):
    # Sky
    screen.fill((135, 206, 235))
    # Sun
    pygame.draw.circle(screen, (255, 255, 0), (width - 80, 80), 50)
    # Clouds
    pygame.draw.ellipse(screen, (255, 255, 255), (100, 60, 120, 50))
    pygame.draw.ellipse(screen, (255, 255, 255), (200, 90, 100, 40))
    pygame.draw.ellipse(screen, (255, 255, 255), (400, 50, 140, 60))

def show_game_over(screen, font, plant_count):
    if plant_count >= 50:
        result_text = "Gold! 50+ plants protected!"
        color = (255, 215, 0)
    elif plant_count >= 40:
        result_text = "Silver! 40+ plants protected!"
        color = (192, 192, 192)
    elif plant_count >= 30:
        result_text = "Bronze! 30+ plants protected!"
        color = (205, 127, 50)
    else:
        result_text = "Try Again! Fewer than 30 plants protected."
        color = (255, 0, 0)
    result_surf = font.render(result_text, True, color)
    screen.blit(result_surf, (WIDTH//2 - result_surf.get_width()//2, HEIGHT//2))

def run_game(student_defense_func):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity Garden Challenge")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    garden = GardenManager(WIDTH, HEIGHT)
    timer = 0
    game_timer = GameTimer(120)
    running = True
    game_over = False

    # Add initial seeds (limit to 10)
    spacing = (WIDTH - 120) // 9  # 10 seeds, 9 spaces
    for i in range(10):
        x = 60 + i * spacing
        garden.add_seed(Seed(x, 50))

    # Immediately update the score after adding seeds
    garden.score_manager.update(garden.seeds)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game_timer.is_time_up():
            game_over = True

        if not game_over:
            timer += 1
            garden.update(timer)
            student_defense_func(garden, timer)

        draw_background(screen, WIDTH, HEIGHT)
        garden.draw(screen)

        # Draw timer
        time_left = game_timer.time_left()
        timer_surf = font.render(f"Time Left: {time_left}s", True, (0, 0, 0))
        screen.blit(timer_surf, (10, 10))

        # Draw score
        plant_count = garden.get_plant_count()
        score_surf = font.render(f"Plants Protected: {plant_count}", True, (0, 100, 0))
        screen.blit(score_surf, (10, 50))

        # Show result at end
        if game_over:
            show_game_over(screen, font, plant_count)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()