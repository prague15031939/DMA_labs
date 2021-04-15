from GrammarBuilder import GrammarBuilder
from Inputter import Inputter

class Regulation:
	def __init__(self, leftPart, rightPart):
		self.leftPart = leftPart
		self.rightPart = rightPart

	def isPartEquals(self, rightPart):
		if len(rightPart) > 1 and len(self.rightPart) > 1 and rightPart[0] == None:
			return self.rightPart[1] == rightPart[1]
		return self.rightPart[:len(rightPart)] == rightPart

	def isRightPartTerminate(self, notTerminate=None):
		if len(self.rightPart) > 1:
			return not self.rightPart[1].startswith('A' if notTerminate == None else notTerminate)
		return False

	def __repr__(self):
		rightNotTerminal = ""
		if len(self.rightPart) != 1:
			rightNotTerminal += f"*{self.rightPart[1]}"
		return f"{self.leftPart}->{self.rightPart[0]}{rightNotTerminal}"

class Regulations:
	def __init__(self):
		self.count = 1
		self.regulations = []

	def getRegulationByParts(self, leftPart=None, rightPart=None):
		result = []
		for i, regulation in enumerate(self.regulations):
			if (leftPart == None and rightPart != None and regulation.isPartEquals(rightPart)) or \
         		(leftPart != None and regulation.leftPart == leftPart and rightPart == None) or \
         		(leftPart != None and regulation.leftPart == leftPart and rightPart != None and regulation.isPartEquals(rightPart)):
				result.append(regulation)
		return result

	def addRegulation(self, leftPart, rightPart):
		self.count += 1
		self.regulations.append(Regulation(leftPart, rightPart))

	def hasRegulation(self, leftPart, rightPart):
		for i, regulation in enumerate(self.regulations):
			if regulation.leftPart == leftPart and regulation.rightPart == rightPart:
				return True
		return False

	def getSymbols(self):
		nonTerminate, terminate = [], []
		for i, regulation in enumerate(self.regulations):
			if not regulation.leftPart in nonTerminate:
				nonTerminate.append(regulation.leftPart)
			if len(regulation.rightPart) > 1 and regulation.rightPart[1].startswith('A') and not regulation.rightPart[1] in nonTerminate:
				nonTerminate.append(regulation.rightPart[1])
			if not regulation.rightPart[0] in terminate:
				terminate.append(regulation.rightPart[0])
		return nonTerminate, terminate

	def renameAll(self, old, new):
		for i, regulation in enumerate(self.regulations):
			if regulation.leftPart == old:
				if self.hasRegulation(new, regulation.rightPart):
					del self.regulations[i]
					self.renameAll(old, new)
					return
				else:
					regulation.leftPart = new
			if len(regulation.rightPart) > 1 and regulation.rightPart == (regulation.rightPart[0], old):
				if self.hasRegulation(regulation.leftPart, (regulation.rightPart[0], new)):
					del self.regulations[i]
					self.renameAll(old, new)
					return
				else:
					regulation.rightPart = (regulation.rightPart[0], new)

	def concatRegulationLenTwo(self):
		for i, regulation in enumerate(self.regulations):
			if regulation.isRightPartTerminate():
				for j, elem in enumerate(self.getRegulationByParts(None, (regulation.rightPart[0],))):
					if not elem.isRightPartTerminate() and len(self.getRegulationByParts(elem.rightPart[1], (regulation.rightPart[1],))) != 0:
						del self.regulations[i]
						self.renameAll(regulation.leftPart, elem.leftPart)
						self.concatRegulationLenTwo()
						return

	def deleteRepeatRegulation(self):
		for i in range(len(self.regulations)):
			for j in range(i + 1, len(self.regulations)):
				if self.regulations[i].rightPart == self.regulations[j].rightPart:
					self.renameAll(self.regulations[j].leftPart, self.regulations[i].leftPart)
					self.deleteRepeatRegulation()
					return

def checkRegulations(regulations, elem, regulationLeftPart):
	name = 'A' + str(regulations.count)
	reg = regulations.getRegulationByParts(regulationLeftPart, (elem[0],))
	if len(elem) != 1:
		if len(reg) != 0 and reg[0].rightPart != elem:
			checkRegulations(regulations, elem[1:], reg[0].rightPart[1])
		else:
			if len(elem) > 2:
				regulations.addRegulation(regulationLeftPart, (elem[0], name))
				checkRegulations(regulations, elem[1:], name)
			else:
				regulations.addRegulation(regulationLeftPart, (elem[0], elem[1]))
	else:
		regulations.addRegulation(regulationLeftPart, (elem[0],))

def main():
	chainList = ['caaab', 'babab', 'caab', 'bbac', 'cab', 'bbb', 'cb']
	regulations = Regulations()
	for i, elem in enumerate(chainList):
		checkRegulations(regulations, chainList[i], 'A0')
	regulations.concatRegulationLenTwo()
	regulations.deleteRepeatRegulation()

	nonTerminate, terminate = regulations.getSymbols()
	for item in regulations.regulations:
		print(item)

if __name__ == "__main__":
	main()
