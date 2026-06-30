class Entity:
    def __init__(self, name, symbol, x, y):
        self.name = name
        self.symbol = symbol
        self.move = None
        self.x = x
        self.y = y
        self.damage = 10
        self.hp = 100
        self.maxhp = 100
        self.armor = 0
        self.hostile = True
        self.speed = 10
        self.gold = 0
        self.alive = True
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