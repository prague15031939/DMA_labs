import numpy as np
from math import sqrt, exp, pi
from random import randint
from statistics import mean

class BayesDivision:

    def __init__(self, pc1, pc2, width=800, height=500):
        self.pc1 = pc1
        self.pc2 = pc2
        self.width = width
        self.height = height
        self.pointAmount = 10000
        self.__offset = 150
        self.__scale = 250000
        self.pointsList1 = []
        self.pointsList2 = []
        self.ordinatsList1 = []
        self.ordinatsList2 = []

    def generateData(self):
        self.pointsList1 = [randint(0, self.width) - self.__offset for i in range(self.pointAmount)]
        self.pointsList2 = [randint(0, self.width) + self.__offset for i in range(self.pointAmount)]

    def findDistributionParams(self):
        mu1 = mean(self.pointsList1)
        mu2 = mean(self.pointsList2)
        sigma1 = sum([(item - mu1) ** 2 for item in self.pointsList1])
        sigma2 = sum([(item - mu2) ** 2 for item in self.pointsList2])
        sigma1 = sqrt(sigma1 / self.pointAmount)
        sigma2 = sqrt(sigma2 / self.pointAmount)

        return mu1, mu2, sigma1, sigma2

    def dividePoints(self, mu1, mu2, sigma1, sigma2):
        for x in range(self.width):
            p1 = exp(-0.5 * (((x - mu1) / sigma1) ** 2)) / (sigma1 * sqrt(2 * pi))
            self.ordinatsList1.append(p1 * self.pc1 * self.__scale)
        for x in range(self.width):
            p2 = exp(-0.5 * (((x - mu2) / sigma2) ** 2)) / (sigma2 * sqrt(2 * pi))
            self.ordinatsList2.append(p2 * self.pc2 * self.__scale)

        return [i for i in range(self.width)], self.ordinatsList1, [i for i in range(self.width)], self.ordinatsList2

    def findErrorValues(self, mu1, mu2, sigma1, sigma2):
        p1 = 1; p2 = 0; x = -self.__offset; eps = 0.01
        falseAlarmError = 0
        missingDetectingError = 0

        while (p2 < p1):
            p1 = self.pc1 * exp(-0.5 * ((x - mu1) / sigma1) ** 2) / (sigma1 * sqrt(2 * pi))
            p2 = self.pc2 * exp(-0.5 * ((x - mu2) / sigma2) ** 2) / (sigma2 * sqrt(2 * pi))
            falseAlarmError += p2 * eps
            x += eps

        border = x

        while (x < self.width + 100):
            p1 = exp(-0.5 * ((x - mu1) / sigma1) ** 2) / (sigma1 * sqrt(2 * pi))
            p2 = exp(-0.5 * ((x - mu2) / sigma2) ** 2) / (sigma2 * sqrt(2 * pi))
            missingDetectingError += p1 * self.pc1 * eps
            x += eps

        return falseAlarmError / self.pc1, missingDetectingError / self.pc1, border
