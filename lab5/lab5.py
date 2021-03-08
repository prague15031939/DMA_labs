from potentials import Potentials

def main():
	workObject = Potentials()
	coefs, srcPoints = workObject.classify()
	testPoints = workObject.generateTestSet(coefs, 250)
	workObject.viewData(coefs, srcPoints, testPoints)

if __name__ == "__main__":
	main()
