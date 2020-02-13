class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class TheToadPrince(Enemy):
    def __init__(self):
        super().__init__("THE TOAD PRINCE", 250, 35)


class TheCareTaker(Enemy):
    def __init__(self):
        super().__init__("THE CARE TAKER", 100, 15)


class TheLocustSwarm(Enemy):
    def __init__(self):
        super().__init__("THE SWARM", 50, 5)
