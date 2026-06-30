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
        # Player spawn
        self.player = Entity('You', '@', 1, 1)
        self.entites = [self.player]
        self.map[self.player.y][self.player.x] = '@'
        # Final
        self.drawMap()

    def moveEntites(self):
        for i in self.entites:
            if not i.move:
                continue
            t = [i.x, i.y]
            match i.move:
                case 'w':
                    t[1]-=1
                case 's':
                    t[1]+=1
                case 'a':
                    t[0]-=1
                case 'd':
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
        return map
                    
    def drawMap(self):
        print()
        for i in self.map:
            print(*i)

    def moveHero(self):
        self.player.move = input('' \
                                'Куда идти? : W/A/S/D : '
                                ).lower()[0]

    def updateWorld(self):
        g.moveHero()
        g.moveEntites()
        g.drawMap()

# hero = Entity('You', '@')
# zombie = Entity('Зомби', 'z')
# print(type(zombie) == Entity)


# def moveEntites():
#    for i in map

# def drawMap():
#   for i in map:
#     print(*i)



# map = initMap(12)
# drawMap()
g = game()
while True:
    g.updateWorld()