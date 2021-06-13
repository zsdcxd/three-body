import random
import star


# from main import stafflist, civnum, dist


class civ(object):
    def __init__(self, civid, starnum):
        from main import civnum
        self.live = 1  # 1存活0死亡
        self.id = civid  # 文明编号
        self.state = random.random() / 2  # 科技水平，0为最低2为最高
        self.speed = random.random() / 20  # 发展速度，遇到其他文明有可能增大
        self.sight = [starnum]  # 观测的星系表
        self.nonesight = list(range(star.starnum))
        self.nonesight.remove(starnum)  # 没观测的星系表
        self.star = [starnum]  # 占领的星系表
        self.sightwithoutciv = []  # 未占领的无文明星系表
        self.sightwithciv = []  # 观测到有文明星系表
        self.nocommunication = list(range(civnum))
        self.nocommunication.remove(self.id)  # 未接触的文明
        self.communication = []  # 建立友好交流的文明
        # self.population = 0.2  # 人口，超过1会移民
        # self.develop = 0.1*len(self.star)  # 文明人口增长速度
        self.character = random.randint(1, 3)  # 1为好斗，2为和平，3为静默
        self.staff = []  # 正在做的事项,格式['动作'，对象,时间,其他]，如['immigrate',12,10],指正在移民12号星系，将在10百年后完成

        star.maplist[starnum]['owner'] = self.id

        pass

    def move(self):
        from main import stafflist , civs
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
        else:
            for i in self.star:
                star.maplist[i]['owner'] = None
            for i in stafflist:
                if i[2] == self.id:
                    stafflist.remove(i)
            for i in civs:
                for star in self.star:
                    if star in civs[i].sightwithciv:
                        civs[i].sightwithciv.remove(star)
                    if star in civs[i].nocommunication:
                        civs[i].nocommunication.remove(star)

            pass
        pass

    # def immigrate(self):
    #     self.star.append(self.sightwithoutciv[random.randint(0, len(self.sightwithoutciv))])
    #     pass

    def search(self):
        distancelist = star.distto(self.id, self.nonesight)
        for i in range(min(max(1, int(self.state * 10)), len(self.nonesight))):
            self.staff.append(['search', distancelist[i][0], distancelist[i][1]])
            self.nonesight.remove(distancelist[i][0])
        pass

    def event(self, event, target, others=None):
        from main import stafflist
        if event == 'search':
            self.sight.append(target)
            if star.maplist[target]['owner'] is None:
                self.sightwithoutciv.append(target)
            else:
                self.sightwithciv.append(target)
                print(star.maplist[target]['owner'], self.nocommunication)
                if star.maplist[target]['owner'] not in self.nocommunication:
                    self.nocommunication.remove(star.maplist[target]['owner'])
                    self.diplomacy(star.maplist[target]['owner'])
            pass
        elif event == 'immigrate':
            star.maplist[target]['owner'] = self.id
            pass
        elif event == 'attack':
            stafflist.append(('attack', self.id, target, self.state))
            pass
        elif event == 'trap':
            stafflist.append(('trap', self.id, target, self.state))

        pass

    def diplomacy(self, target):
        self.sightwithciv.append(target)
        if self.character == 1:
            self.staff.append(['attack', target, star.distance(self.id, target)])
            pass
        elif self.character == 2:
            self.staff.append(['communicate', target, star.distance(self.id, target)])
            pass
        pass

    def trap(self):
        from main import dist
        target = random.sample(self.nocommunication, 1)[-1]
        self.staff.append(['trap', target, dist(self.id, target)])
        pass

    def reply(self, movement, target):
        from main import stafflist
        if self.character == 2:
            if movement == 'communicate':
                if target in self.nonesight:
                    self.nonesight.remove(target)
                stafflist.append(('re_communicate', self.id, target))
            elif movement == 'trap':
                stafflist.append(('re_trap', self.id, target))
                pass
            pass
        pass

    pass
