from library.figures.polygon import IrregularP

class Rectangle(IrregularP):
    def __init__(self, x_o, y_o, x_t, y_t):
        self.x_o = x_o
        self.y_o = y_o
        self.x_t = x_t
        self.y_t = y_t
        super().__init__(self.calculate_edges(), 4)

    def calculate_edges(self):
        return [self.x_o, self.y_o, self.x_t, self.y_o, self.x_t, self.y_t, self.x_o, self.y_t]