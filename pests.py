import pygame
import sys
import time

class Pest:
    SPEED = 2
    EAT_TIME = 1.0  # seconds

    def __init__(self, target_x, terrain, radius=16):
        self.x = 0
        self.target_x = target_x
        self.terrain = terrain
        self.radius = radius
        self.state = "moving"  # "moving", "eating", "done"
        self.eat_start_time = None

    def update(self):
        if self.state == "moving":
            if self.x < self.target_x:
                self.x += self.SPEED
                if self.x >= self.target_x:
                    self.x = self.target_x
                    self.state = "eating"
                    self.eat_start_time = time.time()
            else:
                self.state = "eating"
                self.eat_start_time = time.time()
        elif self.state == "eating":
            if time.time() - self.eat_start_time > self.EAT_TIME:
                self.state = "done"

    def draw(self, surface):
        if self.state == "done":
            return
        x_index = int(self.x)
        # Clamp x_index to valid range
        x_index = max(0, min(x_index, len(self.terrain) - 1))
        y = self.terrain[x_index]
        # Draw ladybug body (red ellipse)
        pygame.draw.ellipse(surface, (220, 0, 0), (int(self.x)-self.radius, int(y)-self.radius, self.radius*2, self.radius))
        pygame.draw.circle(surface, (0, 0, 0), (int(self.x)+self.radius-4, int(y)), self.radius//3)
        pygame.draw.circle(surface, (0, 0, 0), (int(self.x)-4, int(y)-2), 2)
        pygame.draw.circle(surface, (0, 0, 0), (int(self.x)+4, int(y)-2), 2)
        pygame.draw.circle(surface, (0, 0, 0), (int(self.x), int(y)+2), 2)
        pygame.draw.line(surface, (0, 0, 0), (int(self.x), int(y)-self.radius//2), (int(self.x), int(y)+self.radius//2), 2)

    def is_done(self):
        return self.state == "done"

# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    terrain = [200] * 400  # Flat terrain at y=200
    pest = Pest(200, terrain)
    pest.appear()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pest.update()
        screen.fill((255, 255, 255))
        pest.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()