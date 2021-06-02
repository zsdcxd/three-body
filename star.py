import random

mapx = 100  # 地图宽度(百光年)
mapy = 100  # 地图长度(百光年)
density = 10  # 密度，平均星球间隔距离(百光年)
starnum = int(mapx * mapy / (density * density))


def pos():
    posx = random.randint(0, mapx)
    posy = random.randint(0, mapy)
    return posx, posy


def starmap():
    map = []
    for i in range(starnum):
        map.append(pos())
    return map


maplist = []             #pos是位置，owner是占领文明
for i in range(starnum):
    map_i = {'pos': starmap()[i], 'owner': None}
    maplist.append(map_i)
    pass


def distance(star1, star2):       #获取两个星系的距离
    x1 = maplist[star1]['pos'][0]
    y1 = maplist[star1]['pos'][1]
    x2 = maplist[star2]['pos'][0]
    y2 = maplist[star2]['pos'][1]
    dist = int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
    return dist


# distlist = []
# for i in range(starnum):
#     for t in range(i, starnum):
#         dist = {}
#         dist['stars'] = {i, t}
#         dist['dist']= distance(i,t)
#         distlist.append(dist)
#         pass
#     pass

def distto(starid, starlist = starnum):   #获取starlist中各个星系到starid星系的距离，按照距离从小到大排序
    distolist = {}
    l = list(range(starlist))
    l.remove(starid)
    for i in l:
        distolist[i]=distance(i,starid)
        pass
    distolist = sorted(distolist.items(), key=lambda d:d[1])
    return distolist

# print(distto(10))

# print(maplist)
# print(distlist)

