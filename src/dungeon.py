class Dungeon():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[int for i in range(w)] for j in range(h)]

    def SetCell(self, x, y, value):
        self.grid[y][x] = value

    def Generate(self):
        for i in range(self.w):
            for j in range(self.h):
                pass
