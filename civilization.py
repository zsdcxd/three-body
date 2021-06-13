import random
import star as stars


# from main import stafflist, civnum, dist


class civ(object):
    def __init__(self, civid, starnum):
        from main import civnum
        self.live = 1  # 1存活0死亡
        self.id = civid  # 文明编号
        self.state = random.random() / 2  # 科技水平，0为最低2为最高
        self.speed = random.random() / 20  # 发展速度，遇到其他文明有可能增大
        self.stars_in_sight = [starnum]  # 观测的星系表
        self.stars_not_seen = list(range(stars.starnum))
        self.stars_not_seen.remove(starnum)  # 没观测的星系表
        self.stars_landed = [starnum]  # 占领的星系表
        self.stars_without_civ = []  # 未占领的无文明星系表
        self.stars_with_civ = []  # 观测到有其他文明星系表
        self.civ_without_communication = list(range(civnum))
        self.civ_without_communication.remove(self.id)  # 未接触的文明
        self.civ_with_communication = []  # 建立友好交流的文明
        # self.population = 0.2  # 人口，超过1会移民
        # self.develop = 0.1*len(self.star)  # 文明人口增长速度
        self.character = random.randint(1, 3)  # 1为好斗，2为和平，3为静默
        self.staff = []  # 正在做的事项,格式['动作'，对象,时间(距离),其他]，如['immigrate',12,10],指正在移民12号星系，将在10百年后完成

        stars.maplist[starnum]['owner'] = self.id

        pass

    pass

    def move(self):
        from main import stafflist, civs
        if self.live == 1:
            for i in self.staff:
                # print(1, self.id, self.staff, i)
                if i[2] <= 1:
                    self.event(i[0], i[1], i[2:-1])
                    self.staff.remove(i)
                else:
                    # print(2, self.id, self.staff, i)
                    i[2] -= 1
                    pass
                pass
            if self.character == 1:
                if random.random() > 0.7:
                    self.trap()
                    pass
                pass

            self.state += self.speed
            if self.state > 2:
                self.state = 2
            self.search()
        elif self.live == 0:
            for i in civs:
                for star in self.stars_landed:
                    stars.maplist[star]['owner'] = None
                    if star in civs[i].stars_with_civ:
                        civs[i].stars_with_civ.remove(star)
                if self.id in civs[i].civ_without_communication:
                    civs[i].civ_without_communication.remove(self.id)
                if self.id in civs[i].civ_with_communication:
                    civs[i].civ_with_communication.remove(self.id)
            for i in stafflist:
                if i[2] == self.id or i[1] == self.id:
                    stafflist.remove(i)
                pass
            pass
        pass

    pass

    # def immigrate(self):
    #
    # pass

    def search(self):
        distancelist = stars.distto(self.id, self.stars_not_seen)
        for i in range(min(max(1, int(self.state * 10)), len(self.stars_not_seen))):
            self.staff.append(['search', distancelist[i][0], distancelist[i][1]])
            self.stars_not_seen.remove(distancelist[i][0])
        pass

    pass

    def trap(self):
        if self.civ_without_communication:
            from main import dist, civiposlist
            target = random.sample(self.civ_without_communication, 1)[-1]
            self.staff.append(['trap', civiposlist[target], dist(self.id, target)])

    pass

    def reply(self, movement, target_id):
        from main import civs
        from main import stafflist
        if self.character == 2:
            if movement == 'communicate':
                stafflist.append(('re_communicate', self.id, target_id))
            elif movement == 'trap':
                times = 0
                for star in civs[target_id].stars_landed:
                    if star in self.stars_not_seen:
                        times += 1
                pass
                if times == 0:
                    stafflist.append(('re_trap', self.id, target_id))
                pass
            pass
        pass

    pass

    def event(self, event, target_pos, others=None):
        from main import stafflist
        if event == 'search':
            self.stars_in_sight.append(target_pos)
            if stars.maplist[target_pos]['owner'] is None:
                self.stars_without_civ.append(target_pos)
            else:
                self.stars_with_civ.append(target_pos)
                # print(stars.maplist[target]['owner'], self.nocommunication)
                if stars.maplist[target_pos]['owner'] in self.civ_without_communication:
                    self.civ_without_communication.remove(stars.maplist[target_pos]['owner'])
                    self.stars_with_civ.append(stars.maplist[target_pos]['owner'])
                    if self.character == 1:
                        self.staff.append(['attack', target_pos, stars.distance(self.id, target_pos)])
                        pass
                    elif self.character == 2:
                        self.staff.append(['communicate', target_pos, stars.distance(self.id, target_pos)])
                        pass
                    pass
                pass
            pass

        elif event == 'immigrate':
            stars.maplist[target_pos]['owner'] = self.id
            pass

        elif event == 'attack':
            stafflist.append(('attack', self.id, stars.maplist[target_pos]['owner'], self.state))
            pass

        elif event == 'trap':
            stafflist.append(('trap', self.id, stars.maplist[target_pos]['owner'], self.state))
            pass

        pass

    pass
