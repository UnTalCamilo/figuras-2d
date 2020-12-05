import math

class Graph:
    def  __init__(self, screen):
        self.screen = screen
        self.color = (255, 0, 0)
        self.pattern = 0
        

    def style(self, pattern, color):
        if isinstance(pattern, int):
            self.pattern = pattern
            self.color = color


    def pixel(self, pos_one, pos_two):
        self.screen.fill(self.color, ((round(pos_one), round(pos_two)), (1,1)))


    def draw_lines(self, points_s, points_e):
        if len(points_s) <= len(points_e):
            for idx, value in enumerate(points_s):
                self.line(points_s[idx][0], points_s[idx][1], points_e[idx][0], points_e[idx][1])

        else:
            for idx, value in enumerate(points_e):
                self.line(points_s[idx][0], points_s[idx][1], points_e[idx][0], points_e[idx][1])

    def line(self, x_o, y_o, x_t, y_t, draw = True):
        y = y_t - y_o
        x = x_t - x_o
        try:
            m= self.__grq(y, x)
            if abs(y) > abs(x):
                start, end = y_o, y_t
                f = False
            else:
                start, end = x_o, x_t
                f = True
            if start > end:
                start, end = end, start
            return self.__draw_line(start, end, m, x_t, y_t, f, draw)
        except ValueError:
            pass


    def __grq(self, y, x):
        if y == 0 and x == 0:
            raise ValueError
        if x != 0:
            return y/x
        else:
            return math.inf


    def __draw_line(self, start, end, m, x_t, y_t, f, d):
        points = []
        for i in range(start, end + 1):
            if f:
                y = round( m * (i - x_t) + y_t)
                if d:
                    self.pixel(i, y)
                points.append((i,y))
            else:
                x = round(((i - y_t)/m) + x_t)
                if d:
                    self.pixel(x, i)
                points.append((x,i))
        return points