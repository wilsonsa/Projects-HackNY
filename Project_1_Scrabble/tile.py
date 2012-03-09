class Tile:
    def __init__(self, letter, value, row, col):
        self.letter = letter
        self.value = value
        self.row = row
        self.col = col
    def __str__(self):
        return "Tile with letter: %s, value %d, row %d, col %d"% (self.letter, self.value, self.row,self.col)
