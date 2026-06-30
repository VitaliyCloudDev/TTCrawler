#      .-""""""-.
#    .'          '.
#   /   O      O   \
#  :                :
#  |                |   
#  : ',          ,' :
#   \  '-......-'  /
#    '.          .'
#      '-......-'
from entities import Entity

class game:
    def __init__(self):
        # Map init
        self.map_size = 16
        self.map = self.initMap(self.map_size)
        # Final
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
                    raise Exception("NAVERROR")
            if self.map[t[1]][t[0]] != 0:
                continue
            self.map[t[1]][t[0]] = i.symbol
            self.map[i.y][i.x] = 0
            i.x,i.y = t[0],t[1]

    def initMap(self, map_size):
        map = [[0 for i in range(map_size)] for i in range(map_size)]
        # Рисуем края стены карты
        for i in map:
            i[0] = 1
            i[-1] = 1
        map[0] = [1 for i in range(map_size)]
        map[-1] = [1 for i in range(map_size)]
        # Добавляем двери
        map[-1][1] = 2
        map[0][-2] = 2
        # Добавляем персонажа
        self.player = Entity('You', '@', 1, 1)
        self.entites = [self.player]
        map[self.player.y][self.player.x] = '@'
        return map
                    
    def drawMap(self):
        print()
        for i in self.map:
            print(*i)

    def movePlayer(self):
        i = input('' \
                'Куда идти? : W/A/S/D : '
                ).lower()[0]
        match i:
            case 'w':
                dir = 'n'
            case 's':
                dir = 's'
            case 'a':
                dir = 'w'
            case 'd':
                dir = 'e'
            case _:
                dir = None

        self.player.move = dir

    def updateWorld(self):
        g.movePlayer()
        g.moveEntites()
        g.drawMap()

# MAIN
g = game()
while True:
    g.updateWorld()