# Problem ID: 3797
# Title: Design Spreadsheet
# Runtime: 98 ms

class Spreadsheet:

    def __init__(self, rows: int):
        self.mp = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.mp[cell] = value

    def resetCell(self, cell: str) -> None:
        self.mp[cell] = 0

    def getValue(self, formula: str) -> int:
        def getVal(s):
            if s.isnumeric():
                return int(s)
            return self.mp[s]
        return sum(map(getVal,formula[1:].split("+")))



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)