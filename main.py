import pyWinhook
import pythoncom
import random
import civilization
import communication
import star
import civipos

civnum = 10
starnum = star.starnum
civiposlist = random.sample(list(range(1, star.starnum + 1)), civnum)
civs = {}
stafflist = []  # ('attact',self.id,target,self.state)


def move():
    for num in range(len(stafflist)):
        if stafflist[num][2] <= 1:
            event(stafflist[num][0], stafflist[num][1], stafflist[num][2:-1])
            stafflist.pop(num)
        else:
            stafflist[num][2] -= 1
            pass
        pass


def event(movement, id_start, id_part):
    if movement == 'attact':
        if civs[id_start].state > 0.7 * civs[id_part].state:
            civs[id_part].live = 0
        else:
            stafflist.append(('attact', id_part, id_start))
            pass
    elif None:

        pass


for i in range(civnum):
    civ_i = civilization.civilization(i, civiposlist[i])
    civs.update({i: civ_i})
    pass

hm = pyWinhook.HookManager()


def onkeyboardevent(event):
    return True


hm.KeyDown = onkeyboardevent
hm.HookKeyboard()
pythoncom.PumpMessages()
