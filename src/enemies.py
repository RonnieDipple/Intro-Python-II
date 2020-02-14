class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Amarok(Enemy):
    def __init__(self):
        self.name = "AMAROK THE HUNTER"
        self.hp = 300
        self.damage = 50


class TheToadPrince(Enemy):
    def __init__(self):
        self.name = "THE TOAD PRINCE"
        self.hp = 250
        self.damage = 35


class TheCareTaker(Enemy):
    def __init__(self):
        self.name = "THE CARE TAKER"
        self.hp = 100
        self.damage = 15


class TheLocustSwarm(Enemy):
    def __init__(self):
        self.name = "THE SWARM"
        self.hp = 50
        self.damage = 5
