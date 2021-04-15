from GrammarBuilder import GrammarBuilder
from Inputter import Inputter

def main():
	chains = []#Inputter(5).input()
	workObject = GrammarBuilder(chains)
	workObject.entryPoint()

if __name__ == "__main__":
	main()
