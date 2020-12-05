from library.figures.polygon import IrregularP

class RightT (IrregularP):
    
    def __init__(self, x_o, y_o, size_x, size_y):
        self.x = x_o
        self.y = y_o
        self.size_x = size_x
        self.size_y = size_y
        super().__init__(self.calculate_edges(), 3)

    
    def calculate_edges(self):
        return [self.x, self.y, self.x + self.size_x, self.y, self.x, self.y - self.size_y]
    