#      .-""""""-.
#    .'          '.
#   /   O      O   \
#  :                :
#  |                |   
#  : ',          ,' :
#   \  '-......-'  /
#    '.          .'
#      '-......-'
from entities import (
        Entity,
        Zombie,
        )
from random import randint
class NavigationError(ValueError):
    pass

class game:
    def __init__(self):
        # Map init
        self.entites = []
        self.map_size = 16
        self.map = self.initMap(self.map_size)
        # Debug
        self.player.attacks = [['Удар по жопе!',400,100]]
        # Final
        self.frame = None
        self.drawMap()

    def moveEntites(self):
        for i in self.entites:
            if not i.move:
                continue
            t = [i.x, i.y]
            match i.move:
                case 'n':
                    t[1]-=1
                case 's':
                    t[1]+=1
                case 'w':
                    t[0]-=1
                case 'e':
                    t[0]+=1
                case _:
                    raise NavigationError(i.move)
            if self.map[t[1]][t[0]] != ' ':
                continue
            self.map[t[1]][t[0]] = i.symbol
            self.map[i.y][i.x] = ' '
            i.x,i.y = t[0],t[1]
            i.move = None

    def spawnEnemy(self):
        if len(self.entites) > 2:
            return
        x = randint(3,4)
        y = randint(2,5)
        self.entites.append(Zombie(x,y))
    
    def logicEntites(self):
        self.spawnEnemy()
        for i in self.entites:
            if i.hp <= 0:
                i.alive = False
                print(f'{i.name} Погибает!')
                self.map[i.y][i.x] = ' '
                self.entites.remove(i)
                continue
            if i.hostile:
                attackPos = [[-1,0],[0,1],[1,0],[0,-1]]
                coords = [self.player.y - i.y, self.player.x - i.x]
                if coords in attackPos:
                    self.player.attack(i)
                    i.attack(self.player)
            if i.wander:
                i.rMove()
    
    def initMap(self, map_size):
        map = [[' ' for i in range(map_size)] for i in range(map_size)]
        # Рисуем края стены карты
        for i in map:
            i[0] = 1
            i[-1] = 1
        map[0] = [1 for i in range(map_size)]
        map[-1] = [1 for i in range(map_size)]
        # Добавляем двери
        map[-1][1] = 2
        map[0][-2] = 2

        # Добавляем игрока
        if not len(self.entites):
            self.player = Entity('You', '@', 1, 1)
            self.player.wander = False
            self.player.hostile = False
            self.entites.append(self.player)
        map[self.player.y][self.player.x] = self.player.symbol

        return map
                    
    def drawMap(self):
        print()
        for i,v in enumerate(self.map):
            print(*v, self.renderHud(i))
    
    def renderHud(self, i):
        hud = [
            '-- TunTunCrawler --',
            f'HP:{self.player.hp}/'
                +f'{self.player.maxhp} '
                +f'Броня:{self.player.armor}',
            f'В руке: {self.player.holding}',
            f'Инвентарь: {self.player.inventory}',
            f'Монеты: {self.player.gold}',
        ]
        if i >= len(hud):
            return ''
        return hud[i]

    def movePlayer(self):
        i = input('' \
                'Куда идти? : W/A/S/D : '
                )
        match i:
            case 'w':
                dir = 'n'
            case 's':
                dir = 's'
            case 'a':
                dir = 'w'
            case 'd':
                dir = 'e'
            case '':
                dir = None
            case _:
                dir = None

        self.player.move = dir

    def updateWorld(self):
        self.logicEntites()
        self.movePlayer()
        self.moveEntites()
        self.drawMap()

# MAIN
g = game()
while True:
    g.updateWorld()
