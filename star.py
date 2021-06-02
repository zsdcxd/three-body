import random

mapx = 100  # 地图宽度(光年)
mapy = 100  # 地图长度(光年)
density = 10 # 密度，平均星球间隔距离(光年)
starnum = int(mapx*mapy/(density*density))



class star(object):
    def __init__(self):
        self.num = starnum

    def pos(self):
        posx = random.randint(0, mapx)
        posy = random.randint(0, mapy)
        return (posx,posy)

    def starmap(self):
        map = []
        for i in range(self.num):
            map.append(self.pos())
        return map
    pass

map = star()
maplist = map.starmap()
mapdict =dict(zip(list(range(1,starnum+1)),maplist))
# print(mapdict)