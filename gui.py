import pyWinhook
import pythoncom
import os
import turtle
import star
import main


def trans(pos):
    return 8 * star.maplist[pos]['pos'][0], 8 * star.maplist[pos]['pos'][1]


def setup():
    turtle.setup(900, 900)
    turtle.clear()
    turtle.ht()
    turtle.tracer(False)
    pass


def map():
    turtle.color('black')
    for i in star.maplist:
        turtle.pu()
        turtle.goto(8 * i['pos'][0], 8 * i['pos'][1])
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(2)
        turtle.end_fill()
        turtle.update()
        pass
    pass


def civpos():
    colors = ['red', 'green', 'blue']
    for i in main.civs:
        turtle.color(colors[main.civs[i].character - 1])
        turtle.pu()
        turtle.goto(trans(main.civiposlist[i]))
        turtle.pd()
        turtle.begin_fill()
        turtle.circle(5)
        turtle.end_fill()
        pass


def staff(self_pos, self_staff):
    colors = ['yellow', 'red', 'blue', 'brown', 'green']
    movement = {'search': 0, 'attack': 1, 'trap': 2, 'immigrate': 3, 'communicate': 4}
    for i in self_staff:
        if movement[i[0]] != 0:
            turtle.color(colors[movement[i[0]]])
            turtle.pu()
            turtle.goto(trans(self_pos))
            turtle.pd()
            turtle.goto(trans(i[1]))


year = 0

# print('year=', 0, civs[1].state, civs[1].stars_in_sight, civs[1].stars_landed, civs[1].staff)
hm = pyWinhook.HookManager()


def onkeyboardevent(event):
    global year
    year += 1
    # setup()
    for i in main.civs:
        main.civs[i].move()
        # staff(main.civiposlist[i], main.civs[i].staff)
    print('stafflist:', main.stafflist,'civs:',main.civs.keys())
    main.move()
    # map()
    # civpos()
    # turtle.update()
    # print('year=', year, civs[1].state, civs[1].stars_in_sight, civs[1].stars_landed, civs[1].staff)
    print(year)

    return True


hm.KeyDown = onkeyboardevent
hm.HookKeyboard()
pythoncom.PumpMessages()
