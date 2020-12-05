from library.figures.polygon import RegularP

class EquilateralT(RegularP):
    def __init__(self, x_o, y_o, size):
        super().__init__(x_o, y_o, size, 3)