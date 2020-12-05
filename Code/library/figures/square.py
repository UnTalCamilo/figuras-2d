from library.figures.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, x_o, y_o, size):
        super().__init__(x_o, y_o, x_o + size, y_o + size)
