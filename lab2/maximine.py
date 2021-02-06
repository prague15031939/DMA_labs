from random import randint
from math import sqrt
from itertools import combinations
from statistics import mean
from operator import itemgetter

class maximine:

    def __init__(self, imageAmount, width=600, height=500):
        self.imageAmount = imageAmount
        self.canvasWidth = width
        self.canvasHeight = height
        self.classCores = []
        self.imageList = None
        self.__coreColores = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fff799', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080']
        self.__drawFreq = [list(range(4, 15))[::-1]]
        self.__drawFreq += [list(range(10, 21))]

    def generateData(self):
        self.imageList = [[randint(0, self.canvasWidth), randint(0, self.canvasHeight), -1] for i in range(self.imageAmount)]
        self.classCores.append(self.imageList[randint(0, self.imageAmount)])
        self.__generateSecondCore(self.classCores[0])

    def splitByClasses(self):
        for point in self.imageList:
            distances = [self.__findDist(point, classCore) for classCore in self.classCores]
            point[2] = distances.index(min(distances))

    def __generateSecondCore(self, firstCore):
        distances = [self.__findDist(firstCore, point) for point in self.imageList]
        secondCoreIndex = distances.index(max(distances))
        self.classCores.append(self.imageList[secondCoreIndex])

    def __findDist(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def findPotentialCore(self):
        maxDist = 0; maxDistPoint = None

        for tpl in enumerate(self.classCores):
            coreIndex = tpl[0]
            core = tpl[1]
            maxLocalDist = 0; maxLocalDistPoint = None

            for vector in enumerate(self.imageList):
                if vector[1][2] == coreIndex:
                    dist = self.__findDist(vector[1], core)
                    if (dist > maxLocalDist):
                        maxLocalDist = dist
                        maxLocalDistPoint = vector[1]

            if (maxLocalDist > maxDist):
                maxDist = maxLocalDist
                maxDistPoint = maxLocalDistPoint

        return maxDistPoint, maxDist

    def createNewCore(self, potentialCore, thisCoreDist):
        distances = [self.__findDist(tpl[0], tpl[1]) for tpl in combinations(self.classCores, 2)]
        if (thisCoreDist > mean(distances) / 2):
            self.classCores.append(potentialCore)
            return True
        else:
            return False

    def optimizeCores(self):
        for i in range(len(self.classCores)):
            lst = [[vector[0], vector[1]] for vector in self.imageList if vector[2] == i]
            xAverage = mean(list(map(itemgetter(0), lst)))
            yAverage = mean(list(map(itemgetter(1), lst)))
            self.classCores[i] = [xAverage, yAverage, i]

    def viewData(self, canvas):
        canvas.delete("all")

        coef = -1
        if len(self.imageList) > 10000:
            ind = self.__drawFreq[1].index(len(self.imageList) // 1000)
            coef = self.__drawFreq[0][ind]

        for tpl in enumerate(self.imageList):
            vector = tpl[1]
            pointColor = self.__coreColores[vector[2]]
            if (coef == -1) or (coef != -1) and (tpl[0] % coef != 0):
                canvas.create_oval(vector[0] - 1, vector[1] - 1, vector[0] + 1, vector[1] + 1, fill=pointColor, outline="")

        for vector in self.classCores:
            canvas.create_oval(vector[0] - 3, vector[1] - 3, vector[0] + 3, vector[1] + 3, fill="#000000", outline="")
