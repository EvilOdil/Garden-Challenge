import pygame

GRAVITY = 0.4
SEED_COLOR = (200, 100, 40)

class Seed:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0
        self.radius = 5
        self.landed = False
        self.plant_height = 0
        self.dead = False

    def update(self, terrain_height, growth_rate=0.3, max_height=30):
        if self.dead:
            return
        if not self.landed:
            self.dy += GRAVITY
            self.y += self.dy
            if self.y + self.radius >= terrain_height:
                self.y = terrain_height - self.radius
                self.landed = True
        else:
            self.grow(growth_rate)

    def grow(self, growth_rate):
        """Grow the plant by the given rate (no max height limit)."""
        self.plant_height += growth_rate

    def draw(self, screen, max_height=30):
        if self.dead:
            return
        import pygame
        pygame.draw.circle(screen, SEED_COLOR, (int(self.x), int(self.y)), self.radius)
        if self.landed:
            # Draw the plant at its current height (no limit)
            pygame.draw.line(
                screen, (34, 139, 34),
                (int(self.x), int(self.y)),
                (int(self.x), int(self.y) - int(self.plant_height)), 3
            )
