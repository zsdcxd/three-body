import random
import civilization
import star

civnum = 10
starnum = star.starnum
civiposlist = random.sample(list(range(star.starnum)), civnum)
civs = {}  # {civ_id: civ},星系序号civiposlist[id],位置是 star.maplist[civiposlist[id]]['pos']
stafflist = []  # ('attack',self_id,target_id,self.state)


def move():
    print('move')
    for staff in stafflist:
        if staff in stafflist:
            print('staff:', staff)
            stafflist.remove(staff)
            event(staff[0], staff[1], staff[2], staff[3:])


def event(movement, id_start, id_part, start_state=None):
    print('event:', (movement, id_start, id_part, start_state, civs.keys()))
    if movement == 'attack':
        # print('attack')
        if start_state[0] > 0.7 * civs[id_part].state:
            # print('attack_success')
            civs[id_part].live = 0
            civs[id_part].move()
            civs.pop(id_part)
            pass
        pass

    elif movement == 'trap' or 'communicate':
        civs[id_part].reply(movement, id_start)
    elif movement == 're_trap':
        print('re_trapped')
        for stars in civs[id_start].stars_landed:
            civs[id_part].stars_not_seen.remove(stars)

        civs[id_part].staff.append(['attack', civiposlist[id_start],
                                    star.distance(id_part, civiposlist[id_start])])
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

    else:
        print('movement_ERROR:',movement)
        pass


def dist(id_start, id_part):
    return star.distance((random.sample(civs[id_part].stars_landed, 1)[-1]),
                         (random.sample(civs[id_start].stars_landed, 1))[-1])


for i in range(civnum):
    civ_i = civilization.civ(i, civiposlist[i])
    civs.update({i: civ_i})
    pass
