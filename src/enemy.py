class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class TheToadPrince(Enemy):
    def __init__(self):
        super().__init__(name="THE TOAD PRINCE", hp=250, damage=35)

class TheCareTaker(Enemy):
    def __init__(self):
        super().__init__(name="THE CARE TAKER", hp=100, damage=15)

class TheLocustSwarm(Enemy):
    def __init__(self):
        super().__init__(name="THE SWARM", hp=50, damage=5)
