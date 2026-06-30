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

# gopnik = Entity('Gopnik')
# ment = Entity('Ment')
# print(gopnik.name, gopnik.hp)
# print(ment.name, ment.hp)
# print()
# print('ГОПНИК БЬЕТ МЕНТА')
# gopnik.attack(ment)
# print()
# print(gopnik.name, gopnik.hp)
# print(ment.name, ment.hp)

activeEntites = []

hero = Entity('You', '@', 1, 1)
zombie = Entity('Зомби', 'z', -1, -2)
activeEntites.append(hero, zombie)

def initMap(map, map_size):
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

def drawMap():
  for i in map:
    print(*i)

def moveHero():
    hero.move = input('Куда идти? : Left/Up/Right/Down : ').lower()[0]

map = initMap(map,12)
drawMap()