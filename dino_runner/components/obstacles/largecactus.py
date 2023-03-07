from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS
import random

class LargeCactus(Obstacle):
    def __init__(self):
        cactus_type =random.randint(0,2)
        image = LARGE_CACTUS[cactus_type]
        super().__init__(image)
        self.rect.y = 300