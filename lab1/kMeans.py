from random import randint, sample
from math import sqrt
from statistics import mean
from operator import itemgetter

class kMeans:

    def __init__(self, imageAmount, classAmount, width=600, height=500):
        self.imageAmount = imageAmount
        self.classAmount = classAmount
        self.canvasWidth = width
        self.canvasHeight = height
        self.classCores = None
        self.imageList = None
        self.__coreColores = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fff799', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080']
        self.__drawFreq = [list(range(4, 15))[::-1]]
        self.__drawFreq += [list(range(10, 21))]

    def generateData(self):
        self.imageList = [[randint(0, self.canvasWidth), randint(0, self.canvasHeight), -1] for i in range(self.imageAmount)]
        classIndexes = sample(range(self.imageAmount + 1), self.classAmount)
        self.classCores = [self.imageList[i] for i in classIndexes]

    def recognize(self):
        for point in self.imageList:
            self.__findClosestCore(point)

    def refindAllCores(self):
        sameCoresAmount = 0
        for i in range(len(self.classCores)):
            newCore = self.__refindCore(i)
            if ((abs(newCore[0] - self.classCores[i][0]) <= 5) and (abs(newCore[1] - self.classCores[i][1]) <= 5)):
                sameCoresAmount += 1
            self.classCores[i] = newCore

        return sameCoresAmount != len(self.classCores)

    def __refindCore(self, index):
        lst = [[vector[0], vector[1]] for vector in self.imageList if vector[2] == index]
        xAverage = mean(list(map(itemgetter(0), lst)))
        yAverage = mean(list(map(itemgetter(1), lst)))
        return [xAverage, yAverage, index]

    def __findDist(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def __findClosestCore(self, point):
        distances = [self.__findDist(point, classCore) for classCore in self.classCores]
        point[2] = distances.index(min(distances))

    def viewData(self, canvas):
        canvas.delete("all")
        for vector in self.classCores:
            canvas.create_oval(vector[0] - 3, vector[1] - 3, vector[0] + 3, vector[1] + 3, fill="#000000", outline="")

        coef = -1
        if len(self.imageList) > 10000:
            ind = self.__drawFreq[1].index(len(self.imageList) // 1000)
            coef = self.__drawFreq[0][ind]

        for tpl in enumerate(self.imageList):
            vector = tpl[1]
            pointColor = self.__coreColores[vector[2]]
            if (coef == -1) or (coef != -1) and (tpl[0] % coef != 0):
                canvas.create_oval(vector[0] - 2, vector[1] - 2, vector[0] + 2, vector[1] + 2, fill=pointColor, outline="")

        for vector in self.classCores:
            canvas.create_oval(vector[0] - 3, vector[1] - 3, vector[0] + 3, vector[1] + 3, fill="#000000", outline="")
