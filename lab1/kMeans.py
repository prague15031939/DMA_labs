from random import randint, sample
from math import sqrt

class kMeans:

    def __init__(self, imageAmount, classAmount, width=600, height=500):
        self.imageAmount = imageAmount
        self.classAmount = classAmount
        self.canvasWidth = width
        self.canvasHeight = height
        self.classCores = None
        self.imageList = None
        self.coreColores = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fff799', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080']

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
        x = y = count = 0
        for vector in self.imageList:
            if vector[2] == index:
                x += vector[0]
                y += vector[1]
                count += 1
        return [x // count, y // count, index]

    def __findDist(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def __findClosestCore(self, point):
        distances = [self.__findDist(point, classCore) for classCore in self.classCores]
        point[2] = distances.index(min(distances))

    def viewData(self, canvas):
        canvas.delete("all")
        for vector in self.classCores:
            canvas.create_oval(vector[0] - 3, vector[1] - 3, vector[0] + 3, vector[1] + 3, fill="#000000", outline="")
        for vector in self.imageList:
            pointColor = self.coreColores[vector[2]]
            canvas.create_oval(vector[0] - 1, vector[1] - 1, vector[0] + 1, vector[1] + 1, fill=pointColor, outline="")
