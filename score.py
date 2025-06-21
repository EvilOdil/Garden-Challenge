class ScoreManager:
    def __init__(self):
        self.plant_count = 0

    def update(self, seeds):
        self.plant_count = len([s for s in seeds if s.landed and not s.dead])
