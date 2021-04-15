class Inputter:

    def __init__(self, rowCount):
        self.rowCount = rowCount

    def input(self):
        print(f"input {self.rowCount} chains (a, b, c, d)")
        return [str(input("> ")) for i in range(self.rowCount)]
