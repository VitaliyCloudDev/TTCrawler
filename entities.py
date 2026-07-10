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
        self.stay = 0
        self.hp = 100
        self.maxhp = 100
        self.armor = 0

        self.damage = 5
        self.speed = 5
        self.gold = 0
        self.attacks = [['Удар',self.damage,60],
                        ['Критический удар!',self.damage*2,10],
                        ['Промах!',0,30]]

        self.holding = None
        self.inventory = []

    def get_hp(self):
        return f'{self.name} {self.hp}/{self.maxhp}'
    
    def attack(self, target):
        print()
        attack = choices(self.attacks,[i[2] for i in self.attacks])[0]
        print(f'{self.name} {attack[0]} {target.name}')
        self.stay = 3
        d = attack[1] - target.armor
        if d < 0 :
            d = 0
        target.hp -= d
        if d != 0:
            print(f'Нанесено {d} урона! {target.get_hp()}')
        print()

    def __repr__(self):
        return self.symbol

    def rMove(self):
        self.stay -= 1
        if not self.wander:
            return
        if self.stay <= 0:
            self.stay = 0
        else:
            return
        if randint(0,10) > self.speed:
            return
        dir = ['n','s','w','e']
        self.move = choice(dir)

class Zombie(Entity):
    def __init__(self, x,y):
        super().__init__('Zombie', 'z', x,y)
        self.attacks = [['Кусает!',30,30],
                        ['Спотыкается!',0,30],
                        ['Глубокий укус!',60,10],
                        ['Царапает!',5,20],]
