from library.figures.square import Square
import math

class Cube:
    def __init__(self, x_o, y_o, size):
        self.size = size
        self.s1 = Square(x_o, y_o, size)
        self.s2 = self.calculate_s2(x_o, y_o)
        self.edge1 = self.s1.edge
        self.edge2 = self.s2.edge
        

    def draw(self, g):
        self.s1.draw(g)
        self.s2.draw(g)

        for i in range(len(self.edge1)):
            g.line(self.edge1[i].x,self.edge1[i].y,self.edge2[i].x,self.edge2[i].y)

    def calculate_s2(self, x_o, y_o):

        h = round(self.size/3 * math.sin(math.radians(45)))
        l = round(self.size/3 * math.cos(math.radians(45)))
        return Square (x_o + l, y_o - h, self.size)
