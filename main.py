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
civs = []
stafflist = []
for i in range(civnum):
    civ_i = civilization.civilization(i, civiposlist[i])
    civs.append(civ_i)
    pass


hm = pyWinhook.HookManager()
def onkeyboardevent(event):

    return True

hm.KeyDown = onkeyboardevent
hm.HookKeyboard()
pythoncom.PumpMessages()

