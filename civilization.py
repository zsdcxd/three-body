import random
import star


class civilization(object):
    def __init__(self, civid, starnum):
        self.live = 1  # 1存活0死亡
        self.id = civid  # 文明编号
        self.state = random.random() / 2  # 科技水平，0为最低1为最高
        self.speed = random.random()  # 发展速度，遇到其他文明有可能增大
        self.sight = [starnum]  # 观测的星系表
        self.star = [starnum]  # 占领的星系表
        self.sightwithoutciv = [starnum]  # 观测的无文明星系表
        self.population = 0.2  # 人口，超过1会移民
        self.develop = 0.1*len(self.star)  # 文明人口增长速度
        self.character = random.randint(1, 3)  # 1为好斗，2为和平，3为静默

        star.maplist[starnum]['owner'] = self.id
        pass

    def population(self):
        self.population = self.population + self.develop
        if self.population >= 1:
            self.population -= 1
            self.immigrate()
            pass

        pass

    def immigrate(self):
        self.star.append(self.sightwithoutciv[random.randint(0, len(self.sightwithoutciv))])
        pass

    def search(self):
        for i in range(max(1, int(self.state * 10))):
            self.sight.append(star.maplist)
        pass
