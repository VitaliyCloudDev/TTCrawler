from random import (
    choice,
    choices,
    randint,
)

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
        self.speed = 5
        self.gold = 0
        self.attacks = [['Удар',self.damage],
                        ['Критический удар!',self.damage*2],
                        ['Промах!',0]]
        self.attacks_weight = [
            60,
            10,
            30,
        ]

        self.holding = None
        self.inventory = []

    def get_hp(self):
        return f'{self.name} {self.hp}/{self.maxhp}'
    
    def attack(self, target):
        print(f'{self.name} Атакует {target.get_hp()}!')
        attack = choices(self.attacks,self.attacks_weight)[0]
        d = attack[1] - target.armor
        if d < 0 :
            d = 0
        target.hp -= d
        if target.hp <= 0:
            target.alive = False
        print(f'{attack[0]}')
        if d != 0:
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