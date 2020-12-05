
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Bounds:

        def __init__(self, mn, mx):
            self.mx = mx
            self.mn = mn



class Circle:
    
    def __init__(self, x_o, y_o, radius):
        self.center = Point(x_o, y_o)
        self.radius = radius
        self.points = []
        self.points_x = {}
        self.points_y = {}


    def  __fill_dictionary(self):
        if len(self.points_x) == 0:
            tmp_points_x = {}
            tmp_points_y = {}

            for p in self.points:

                if p.x not in tmp_points_x:
                    tmp_points_x[p.x] = []

                if p.y not in tmp_points_y:
                    tmp_points_y[p.y] = []

                tmp_points_x[p.x].append(p)
                tmp_points_y[p.y].append(p)

            for key, value in tmp_points_x.items():
                self.points_x[key] = self.min_max_y(value)

            for key, value in tmp_points_y.items():
                self.points_y[key] = self.min_max_x(value)
    


    def min_max_x(self, l):
        mx, mn = None, None
        for p in l:
            if mx is None:
                mx, mn = p, p
            if p.x > mx.x:
                mx = p
            if p.x < mn.x:
                mn = p

        return Bounds(mn, mx)

    def min_max_y(self, l) :
        mx, mn = None, None
        for p in l:
            if mx is None:
                mx, mn = p, p
            if p.y > mx.y:
                mx = p
            if p.y < mn.y:
                mn = p

        return Bounds(mn, mx)

    def clean(self):
        self.points.clear()
        self.points_x.clear()
        self.points_y.clear()


    def draw(self, g):
        self.clean()
        x, y = 0, self.radius
        pk = 3 - 2 * self.radius

        self.add_point(self.center.x, self.center.y, x, y)
        self.draw_circle(g, self.center.x, self.center.y, x, y)
        while x <= y:
            x += 1

            if pk <= 0:
                pk = pk + 4 * x + 6
            else:
                y -= 1
                pk = pk + 4 * (x - y) + 10

            self.add_point(self.center.x, self.center.y, x , y)
            self.draw_circle(g, self.center.x, self.center.y, x, y)

        self.fill(g)

    
    def add_point(self, xc, yc, x, y):
        self.points.append(Point(xc + x, yc + y))
        self.points.append(Point(xc - x, yc + y))
        self.points.append(Point(xc + x, yc - y))
        self.points.append(Point(xc - x, yc - y))
        self.points.append(Point(xc + y, yc + x))
        self.points.append(Point(xc - y, yc + x))
        self.points.append(Point(xc + y, yc - x))
        self.points.append(Point(xc - y, yc - x))

    
    def draw_circle(self, g, xc, yc, x, y):
        g.pixel(xc + x, yc + y)
        g.pixel(xc - x, yc + y)
        g.pixel(xc + x, yc - y)
        g.pixel(xc - x, yc - y)
        g.pixel(xc + y, yc + x)
        g.pixel(xc - y, yc + x)
        g.pixel(xc + y, yc - x)
        g.pixel(xc - y, yc - x)
    


    def fill(self, g):
        self.__fill_dictionary()
        pattern = g.pattern
        if pattern  == 1: #all
            
            for key, value in self.points_y.items():
                y = key
                for x in range(value.mn.x, value.mx.x):
                    g.pixel(x, y)


        if pattern  == 2: # h_lines
            
            for key, value in self.points_y.items():
                y = key
                if y % 10 == 0:
                    for x in range(value.mn.x, value.mx.x):
                        g.pixel(x, y)

        
        if pattern  == 3: #v_lines
            
            for key, value in self.points_x.items():
                x = key
                if x % 10 == 0:
                    for y in range(value.mn.y, value.mx.y):
                        g.pixel(x, y)

        if pattern == 4: # h_v lines

            for key, value in self.points_y.items():
                y = key
                for x in range(value.mn.x, value.mx.x):
                    if y % 10 == 0 or x % 10 == 0:
                        g.pixel(x, y)

        if pattern  == 5: # d_p lines
            
            for key, value in self.points_y.items():
                y = key
                if y % 10 == 0:
                    x_o, y_o = self.rotate_point(self.center, value.mn, 45)
                    x_t, y_t = self.rotate_point(self.center, value.mx, 45)
                    g.line(x_o, y_o, x_t, y_t)


        if pattern  == 6: #d_s lines
            
            for key, value in self.points_x.items():
                y = key
                if y % 10 == 0:
                    x_o, y_o = self.rotate_point(self.center, value.mn, -45)
                    x_t, y_t = self.rotate_point(self.center, value.mx, -45)
                    g.line(x_o, y_o, x_t, y_t)

        if pattern == 7: #d P&S lines

            for key, value in self.points_y.items():
                y = key
                if (y % 10 == 0  and y != self.center.y - self.radius and y != self.center.y + self.radius):
                    x_o1, y_o1 = self.rotate_point(self.center, value.mn, 45)
                    x_t1, y_t1 = self.rotate_point(self.center, value.mx, 45)
                    x_o2, y_o2 = self.rotate_point(self.center, value.mn, -45)
                    x_t2, y_t2 = self.rotate_point(self.center, value.mx, -45)
                    g.line(x_o1, y_o1, x_t1, y_t1)
                    g.line(x_o2, y_o2, x_t2, y_t2)



    def rotate_point(self, origin, point, angle):
        #Rotate a point counterclockwise by a given angle around a given origin.
        # The angle should be given in radians.
        ox, oy = origin.x, origin.y
        px, py = point.x, point.y

        dx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        dy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return round(dx), round(dy)