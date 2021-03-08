from random import randint

class Perceptron:

    def __init__(self):
        self.classes = []
        self.weigths = []
        self.__maxRand = 10

    def generateData(self, classNumber, objectPerClass, attrPerObject):
        self.classes = [[[int(randint(0, self.__maxRand) - self.__maxRand / 2) for k in range(attrPerObject)] for j in range(objectPerClass)] for i in range(classNumber)]
        self.weights = [[0 for j in range(attrPerObject + 1)] for i in range(classNumber)]

        for cls in self.classes:
            for object in cls:
                object.append(1)

    def findDecisionFunctions(self):
        isClassification = True; i = 0
        while isClassification and (i < 1000):
            i += 1; notCorrected = 0
            for cls in enumerate(self.classes):
                for obj in cls[1]:
                    if not self.__correctWeight(obj, self.weights[cls[0]], cls[0]):
                        notCorrected += 1
            if (notCorrected == len(self.classes) * len(self.classes[0])):
                isClassification = False

        return i < 1000

    def __correctWeight(self, obj, weight, classNumber):
        objectDecision = self.__multiplyVectors(weight, obj)

        currentDecision = 0; chk = False
        for w in enumerate(self.weights):
            currentDecision = self.__multiplyVectors(w[1], obj)
            if w[0] != classNumber:
                if objectDecision <= currentDecision:
                    self.__changeWeight(w[1], obj, -1)
                    chk = True

        if chk:
            self.__changeWeight(weight, obj)

        return chk

    def __changeWeight(self, weight, obj, sign=1):
        for atr in enumerate(weight):
            weight[atr[0]] += sign * obj[atr[0]]

    def __multiplyVectors(self, v1, v2):
        return sum([i * j for i, j in zip(v1, v2)])

    def findObjectClass(self, obj):
        obj.append(1)
        results = [self.__multiplyVectors(w, obj) for w in self.weights]
        return results.index(max(results)) + 1

    def printClasses(self):
        for cls in enumerate(self.classes):
            print(f"class #{cls[0] + 1}:")
            for obj in cls[1]:
                print(f"\t{obj[:len(obj) - 1]}")

    def printDecisionFunctions(self, view="funcs"):
        if view == "funcs":
            print("decision functions:")
            for w in enumerate(self.weights):
                expr = ""
                for item in enumerate(w[1]):
                    if (item[1] > 0) and (item[0] != 0):
                        expr += "+"
                    expr += f"{item[1]}"
                    if (item[0] != len(w[1]) - 1):
                        expr += f"*x{item[0] + 1} "
                print(f"\td{w[0] + 1}(x) = {expr}")
        elif view == "coefs":
            print("desicion weights:")
            for w in self.weights:
                print(w)
