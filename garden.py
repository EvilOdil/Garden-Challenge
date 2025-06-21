import random
import time  # <-- Add this import
from seed import Seed
from score import ScoreManager
from pests import Pest

class GardenManager:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.GROUND_HEIGHT = 100
        self.terrain = self.generate_terrain()
        self.seeds = []
        self.eaten_plants = 0
        self.score_manager = ScoreManager()
        self.pests = []
        self.growth_rate = 0.3
        self.max_plant_height = 30
        self._seed_plant_times = []  # <-- Track seed plant times

    def generate_terrain(self):
        base_y = self.HEIGHT - self.GROUND_HEIGHT
        return [base_y + int(random.uniform(-10, 10)) for _ in range(self.WIDTH)]

    def add_seed(self, seed):
        self.seeds.append(seed)

    def plant_seed(self, x=None, y=50):
        """Plant a new seed at (x, y). If x is None, choose a random x.
        Limit to 5 seeds per second. Destroy 1 plant if exceeded."""
        now = time.time()
        # Remove timestamps older than 1 second
        self._seed_plant_times = [t for t in self._seed_plant_times if now - t < 1]
        if len(self._seed_plant_times) >= 5:
            print("Seed planting rate limit reached (5 per second). Destroying 1 plant!")
            self.animate_destroy_plants(1)  # Only destroy 1 plant
            return  # Do not plant more than 5 seeds per second
        self._seed_plant_times.append(now)
        if x is None:
            x = random.randint(20, self.WIDTH - 20)
        self.add_seed(Seed(x, y))

    def animate_destroy_plants(self, count):
        """Mark up to 'count' plants for destruction animation."""
        destroyable = [s for s in self.seeds if not getattr(s, 'destroying', False) and not s.dead]
        for seed in destroyable[:count]:
            seed.destroying = True
            seed.destroy_timer = 30  # frames for animation (adjust as needed)

    def set_growth_rate(self, rate, max_height = 30):
        """Set the growth rate for all plants."""
        if rate is None:
            rate = self.growth_rate
        for seed in self.seeds:
            if seed.landed and not seed.dead:
                seed.plant_height = max(seed.plant_height + rate, max_height)


    def grow_all_plants(self, amount=None,max_height = 30):
        """Grow all landed, living plants by 'amount' or by self.growth_rate."""
        if amount is None:
            amount = self.growth_rate
        for seed in self.seeds:
            if seed.landed and not seed.dead:
                seed.plant_height = min(seed.plant_height + amount, max_height)

    def freeze_plants(self):
        """Prevent all plants from growing this frame."""
        for seed in self.seeds:
            seed._frozen = True  # Add a custom attribute

    def unfreeze_plants(self):
        """Allow plants to grow again."""
        for seed in self.seeds:
            if hasattr(seed, '_frozen'):
                del seed._frozen

    def bug_spray(self):
        """Kill one bug (the first pest in the list)."""
        if self.pests:
            self.pests.pop(0)

    def freeze_bugs(self, frames=120):
        """Freeze all bugs for a number of frames (default 2 seconds at 60fps)."""
        for pest in self.pests:
            pest.frozen_until = frames  # Add a custom attribute

    def update(self, timer):
        # 🐞 Ladybug attacks every 10 seconds
        if timer % 600 == 0:
            self.pest_attack()

        # Update pests
        for pest in self.pests:
            # Handle freezing
            if hasattr(pest, 'frozen_until') and pest.frozen_until > 0:
                pest.frozen_until -= 1
                continue  # Skip update if frozen
            pest.update()
        # Remove pests that are done
        self.pests = [p for p in self.pests if not p.is_done()]

        # Remove plants only when pest is eating and at the plant
        for pest in self.pests:
            if pest.state == "eating":
                for s in self.seeds:
                    s_x = max(0, min(int(s.x), len(self.terrain) - 1))
                    pest_x = max(0, min(int(pest.x), len(self.terrain) - 1))
                    if (
                        s.landed and not s.dead and 
                        abs(s.x - pest.x) < 4 and 
                        abs(self.terrain[s_x] - self.terrain[pest_x]) < 8 and
                        s.plant_height >= self.max_plant_height
                    ):
                        s.dead = True
                        self.eaten_plants += 1
        # Actually remove dead plants from the list
        self.seeds = [s for s in self.seeds if not s.dead]

        # Animate destroying plants
        for seed in self.seeds:
            if getattr(seed, 'destroying', False):
                seed.destroy_timer -= 1
                # Optional: animate (e.g., shrink plant_height)
                seed.plant_height = max(0, seed.plant_height - (seed.plant_height / max(1, seed.destroy_timer)))
                if seed.destroy_timer <= 0:
                    seed.dead = True

        # Actually remove dead plants from the list
        self.seeds = [s for s in self.seeds if not s.dead]

        # Plants: skip growth if frozen
        for seed in self.seeds:
            x_index = int(seed.x)
            # Clamp x_index to valid range
            x_index = max(0, min(x_index, len(self.terrain) - 1))
            terrain_y = self.terrain[x_index]
            if hasattr(seed, '_frozen') and seed._frozen:
                continue
            seed.update(terrain_y, growth_rate=self.growth_rate, max_height=self.max_plant_height)

        self.score_manager.update(self.seeds)

    def draw(self, screen):
        for x, y in enumerate(self.terrain):
            screen.set_at((x, y), (139, 69, 19))  # Soil

        for seed in self.seeds:
            seed.draw(screen, max_height=self.max_plant_height)

        # Draw pests
        for pest in self.pests:
            pest.draw(screen)

    def pest_attack(self):
        grown = [s for s in self.seeds if s.landed and not s.dead]
        if not grown:
            return
        max_attack = max(1, int(len(grown) * 1))  # Ensure integer
        num_attacked = random.randint(1, max_attack)
        victims = random.sample(grown, num_attacked)

        used_x = set()
        for s in victims:
            # Ensure ladybugs don't overlap by spacing out their targets
            if int(s.x) in used_x:
                continue
            used_x.add(int(s.x))
            pest = Pest(int(s.x), self.terrain)
            self.pests.append(pest)
        print(f"🐞 Ladybug attack! {num_attacked} plants targeted.")

    def get_plant_count(self):
        return self.score_manager.plant_count

    def set_max_plant_height(self, height):
        """Set the maximum height for all plants and adjust current heights if needed."""
        self.max_plant_height = height
        # Adjust all existing plants to not exceed the new max height
        for seed in self.seeds:
            if seed.plant_height > height:
                seed.plant_height = height

    def set_timer(self, timer_obj):
        """Attach a timer object (e.g., GameTimer) to the garden."""
        self._timer = timer_obj

    def get_time_left(self):
        """Return the time left in seconds, if a timer is attached."""
        if hasattr(self, '_timer'):
            return self._timer.time_left()
        return None
