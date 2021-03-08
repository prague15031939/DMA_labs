import matplotlib.pyplot as plt
import numpy as np
from random import randint, uniform

class Potentials:

    def __init__(self):
        self.points = [[-1, 0, "1"], [1, 1, "1"], [1, 2, "1"], [2, 0, "2"], [1, -2, "2"], [0, -3, "2"]]
        self.potentialCoefs = [1, 4, 4, 16]

    def potentialFunc(self, p, coefs):
        return coefs[0] + p[0] * coefs[1] + p[1] * coefs[2] + p[0] * p[1] * coefs[3]

    def classify(self):
        p = 1
        nextCoefs = [0 for i in range(4)]
        for i in range(len(self.points)):
            coefs = self.potentialCoefs.copy()
            coefs[1] *= self.points[i][0]
            coefs[2] *= self.points[i][1]
            coefs[3] *= self.points[i][0]
            coefs[3] *= self.points[i][1]
            nextCoefs = [item[0] + p * item[1] for item in zip(nextCoefs, coefs)]
            print(nextCoefs)
            if i + 1 < len(self.points):
                res = self.potentialFunc(self.points[i + 1], nextCoefs)
                if (res <= 0) and self.points[i + 1][2] == "1":
                    p = 1
                elif (res > 0) and self.points[i + 1][2] == "2":
                    p = -1
                else:
                    p = 0
            print(f"p: {p}; pFunc: {res}")
        return nextCoefs, self.points

    def generateTestSet(self, coefs, size=100):
        points = [[uniform(-5, 5), uniform(-5, 5)] for i in range(size)]
        for p in points:
            if self.potentialFunc(p, coefs) > 0:
                p.append("1")
            else:
                p.append("2")

        return points

    def viewData(self, coefs, srcPoints, testPoints, title=None):
        for p in srcPoints:
            if p[2] == "1":
                c = "tab:orange"
            elif p[2] == "2":
                c = "tab:green"
            plt.scatter(p[0], p[1], color=c, marker="X", s=50)

        x1 = list(np.linspace(-5, 5, 300))
        y1 = np.array([-(coefs[0] + coefs[1] * item) / (coefs[2] + coefs[3] * item) for item in x1])
        threshold = 20
        y1 = np.ma.masked_less(y1, -1 * threshold)
        y1 = np.ma.masked_greater(y1, threshold)
        plt.plot(x1, y1, label="first", color="tab:red")

        for p in testPoints:
            if p[2] == "1":
                c = "tab:blue"
            elif p[2] == "2":
                c = "tab:purple"
            plt.scatter(p[0], p[1], color=c, s=14)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.title(title)
        plt.legend(loc='lower right')
        plt.show()
