import math
import random
from Monsters.Dragon import Dragon  # Import other Monster classes as needed
from Monsters.Monster import Monster
from Monsters.Worm import Worm  # Import other Monster classes as needed


class MonsterFactory:
    __MONSTER_NAMES = ["Dragon", "Worm"]

    @staticmethod
    def log_based_stats(x):
        return {
            "health": int(20 + 50 * math.log2(x)),
            "attack": int(20 + 8 * math.log2(x)),
            "defense": int(20 + 5 * math.log2(x)),
        }

    @staticmethod
    def create_random_monster(monster_kill_count) -> Monster:
        random_name = random.choice(MonsterFactory.__MONSTER_NAMES)
        monster_type = random.choice([Dragon, Worm])

        x = random.randint(10, 20)
        x += monster_kill_count

        if x > 30:
            x = random.randint(30, 60)

        monster_stats = MonsterFactory.log_based_stats(x)

        return monster_type(name=random_name, **monster_stats)
