import pyWinhook
import pythoncom
import random
import civilization
import star
import os

civnum = 10
starnum = star.starnum
civiposlist = random.sample(list(range(star.starnum)), civnum)
civs = {}  # {civ_id: civ},星系序号civiposlist[id],位置是 star.maplist[civiposlist[id]]['pos']
stafflist = []  # ('attack',self_id,target_id,self.state)


def move():
    for staff in stafflist:
        if i in stafflist:
            stafflist.remove(staff)
            event(staff[0], staff[1], staff[2], staff[3:])


def event(movement, id_start, id_part, start_state=None):
    print(movement, id_start, id_part, start_state, civs)
    if movement == 'attack':
        if start_state[0] > 0.7 * civs[id_part].state:
            civs[id_part].live = 0
            civs[id_part].move()
            civs.pop(id_part)
            pass
        pass

    elif movement == 'trap' or 'communicate':
        civs[id_part].reply(movement, id_start)
    elif movement == 're_trap':
        for stars in civs[id_start].stars_landed:
            civs[id_part].stars_not_seen.remove(stars)
        pass
        civs[id_part].staff.append(['attack', star.maplist[id_start]['pos'],
                                    star.distance(id_part, star.maplist[id_start]['pos'])])
    elif movement == 're_communicate':
        civs[id_start].speed += civs[id_part].speed / 40
        civs[id_part].speed += civs[id_start].speed / 40
        civs[id_part].state += civs[id_start].state / 5
        civs[id_start].state += civs[id_part].state / 5
        civs[id_start].civ_with_communication.append(id_part)
        civs[id_part].civ_with_communication.append(id_start)
        for stars in civs[id_start].stars_landed:
            civs[id_part].stars_not_seen.remove(stars)
        for stars in civs[id_part].stars_landed:
            civs[id_start].stars_not_seen.remove(stars)

        pass


def dist(id_start, id_part):
    return star.distance((random.sample(civs[id_part].stars_landed, 1)[-1]),
                         (random.sample(civs[id_start].stars_landed, 1))[-1])


for i in range(civnum):
    civ_i = civilization.civ(i, civiposlist[i])
    civs.update({i: civ_i})
    pass

year = 0

# print('year=', 0, civs[1].state, civs[1].stars_in_sight, civs[1].stars_landed, civs[1].staff)
hm = pyWinhook.HookManager()


def onkeyboardevent(event):
    global year
    year += 1
    for i in civs:
        civs[i].move()
    move()
    # print('year=', year, civs[1].state, civs[1].stars_in_sight, civs[1].stars_landed, civs[1].staff)
    print(year)

    return True


hm.KeyDown = onkeyboardevent
hm.HookKeyboard()
pythoncom.PumpMessages()
