import random
import star


class civilization(object):
    def __init__(self, civid, starnum):
        self.live = 1  # 1存活0死亡
        self.id = civid  # 文明编号
        self.state = random.random() / 2  # 科技水平，0为最低1为最高
        self.speed = random.random()  # 发展速度，遇到其他文明有可能增大
        self.sight = [starnum]  # 观测的星系表
        self.nonesight = list(range(star.maplist))
        self.nonesight.pop(self.id) #没观测的星系表
        self.star = [starnum]  # 占领的星系表
        self.sightwithoutciv = []  # 未占领的无文明星系表
        self.sightwithciv = []   #观测到有文明星系表
        self.communication = []   #建立友好交流的文明
        # self.population = 0.2  # 人口，超过1会移民
        # self.develop = 0.1*len(self.star)  # 文明人口增长速度
        self.character = random.randint(1, 3)  # 1为好斗，2为和平，3为静默
        self.staff = []  #正在做的事项,格式（'动作'，'对象',时间,其他），如('immigrate','12',10),指正在移民12号星系，将在10百年后完成

        star.maplist[starnum]['owner'] = self.id

        pass

    # def population(self):
    #     self.population = self.population + self.develop
    #     if self.population >= 1:
    #         self.population -= 1
    #         self.immigrate()
    #         pass
    #
    #     pass

    # def immigrate(self):
    #     self.star.append(self.sightwithoutciv[random.randint(0, len(self.sightwithoutciv))])
    #     pass

    def diplomacy(self,target):
        if self.character == 1:
            self.staff.append(('attact',target,star.distto(self.id,target),self.state))
            pass
        elif self.character == 2:
            self.communicate(target)
            pass
        else:
            pass

        pass

    def communicate(self,target):
        pass



    def search(self):
        distancelist = star.distto(self.id, self.nonesight)
        for i in range(max(1, int(self.state * 10))):
            self.staff.append(('search',distancelist[0][0],distancelist[0][1]))
        pass

    def event(self,event,target,others=None):
        if event == 'search':
            self.sight.append(target)
            self.nonesight.remove(target)
            if star.maplist[target]['owner'] == None:
                self.sightwithoutciv.append(target)
            else:
                self.sightwithciv.append(target)
                self.diplomacy(target)
            pass
        if event == 'immigrate':
            star.maplist[target]['owner']=self.id
            pass
        if event == 'attact':
            pass

        pass

    def move(self):
        for i in range(len(self.staff)):
            if self.staff[i][2] <= 1 :
                self.event(self.staff[i][0],self.staff[i][1])
                self.staff.pop(i)
            else:
                self.staff[i][2] -= 1
                pass
            pass
