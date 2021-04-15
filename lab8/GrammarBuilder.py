#inport

#
# production = [nonTerminal, terminalString, nextNonTerminal]
#

class GrammarBuilder:

    def __init__(self, chainList):
        self.defaultChainList = ["caaab", "bbaab", "caab", "bbab", "cab", "bbb", "cb"]
        self.chainList = chainList
        self.maxChainLength = max([len(item) for item in self.defaultChainList])
        self.nonTerminals = [f"A{i}" for i in range(1, 101)]
        self.productions = []

    def entryPoint(self):
        self.defaultChainList.sort(key=len, reverse=True)
        nonTerminalIndex = 0
        for chain in self.defaultChainList:
            nonTerminal = "S"
            for terminalTuple in enumerate(chain):
                terminal = terminalTuple[1]

                isRemainder = False
                if (len(chain) == self.maxChainLength) and (terminalTuple[0] == len(chain) - 2):
                    terminal += chain[terminalTuple[0] + 1]
                    isRemainder = True

                production = [nonTerminal, terminal, self.nonTerminals[nonTerminalIndex]]
                nextNonTerminal = self.__getProductionNextNonTerminal(production)
                if (nextNonTerminal == None) or (len(chain) == self.maxChainLength):
                    if not isRemainder:
                        nonTerminal = self.nonTerminals[nonTerminalIndex]
                        nonTerminalIndex += 1
                    else:
                        production[2] = ""
                    self.productions.append(production)
                else:
                    nonTerminal = nextNonTerminal

                if isRemainder:
                    break

        self.viewProductions()

    def __getProductionNextNonTerminal(self, production):
        for item in self.productions:
            if (production[0] == item[0]) and (production[1] == item[1]):
                return item[2]
        return None

    def viewProductions(self):
        for production in self.productions:
            timesSymbol = "*" if production[2] != "" else ""
            print(f"{production[0]}->{production[1]}{timesSymbol}{production[2]}")
