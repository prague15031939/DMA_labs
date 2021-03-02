from perceptron import Perceptron

def main():
	cls = int(input("class amount: "))
	objPerCls = int(input("object per class: "))
	attrPerObj = int(input("attribute per object: "))

	workObject = Perceptron()
	while True:
		workObject.generateData(cls, objPerCls, attrPerObj)
		if workObject.findDecisionFunctions():
			break

	workObject.printClasses()
	workObject.printDecisionFunctions("funcs")

	while True:
		src = input(f"test dataset({attrPerObj} int numbers): ")
		if src == "exit":
			break
		try:
			testDataset = [int(item) for item in src.split(" ")]
			classNumber = workObject.findObjectClass(testDataset)
			print(f"class #{classNumber}")
		except ValueError:
			print("invalid input")

if __name__ == "__main__":
	main()
