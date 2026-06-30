from random import choice

class Entity:
    def __init__(self, name, symbol, x, y):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.hostile = True
        self.alive = True

        self.move = None
        self.wander = True
        self.hp = 100
        self.maxhp = 100
        self.armor = 0

        self.damage = 5
        self.speed = 10
        self.gold = 0

        self.holding = None
        self.inventory = []
        
    def get_hp(self):
        return f'{self.name} {self.hp}/{self.maxhp}'
    def attack(self, target):
        print(f'{self.name} Атакует {target.get_hp()}!')
        d = self.damage - target.armor
        if d < 0 :
            d = 1
        target.hp -= d
        print(f'Нанесено {d} урона! {target.get_hp()}')
    def __repr__(self):
        return self.symbol

    def rMove(self):
        if not self.wander:
            return
        if randint(0,10) > self.speed:
            return
        dir = ['n','s','w','e']
        self.move = choice(dir)