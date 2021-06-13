import pyWinhook
import pythoncom
import random
import civilization
import star
import os

civnum = 10
starnum = star.starnum
civiposlist = random.sample(list(range(star.starnum)), civnum)
civs = {}  # {i: civ_i}
stafflist = []  # ('attack',self.id,target,self.state)


def move():
    for num in range(len(stafflist)):
        event(stafflist[num][0], stafflist[num][1], stafflist[num][2], stafflist[num][2, -1])
        stafflist.pop(num)


def event(movement, id_start, id_part, start_state=None):
    if movement == 'attack':
        if start_state[0] > 0.7 * civs[id_part].state:
            civs[id_part].live = 0
            civs[id_part].move()
            civs.pop(id_part)

        else:
            stafflist.append(['attack', id_part, id_start,civs[id_part].state])
            pass
    elif movement == 'trap' or 'communicate':
        civs[id_part].reply(movement, id_start)
    elif movement == 're_trap':
        civs[id_part].diplomacy(id_start)
    elif movement == 're_communicate':
        civs[id_start].speed += civs[id_part].speed / 40
        civs[id_part].speed += civs[id_start].speed / 40
        civs[id_part].state += civs[id_start].state / 5
        civs[id_start].state += civs[id_part].state / 5

        pass

def dist(id_start,id_part):
    return star.distance((random.sample(civs[id_part].star, 1)[-1]),(random.sample(civs[id_start].star, 1))[-1])


for i in range(civnum):
    civ_i = civilization.civ(i, civiposlist[i])
    civs.update({i: civ_i})
    pass

hm = pyWinhook.HookManager()


print(civs[1].state, civs[1].sight, civs[1].star, civs[1].staff)
def onkeyboardevent(event):
    for i in range(civnum):
        civs[i].move()
    move()
    print(civs[1].state, civs[1].sight, civs[1].star, civs[1].staff)

    return True


hm.KeyDown = onkeyboardevent
hm.HookKeyboard()
pythoncom.PumpMessages()
