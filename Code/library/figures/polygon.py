
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __str__(self):
        return str(self.x)+"---"+str(self.y)



class IrregularP:
    def __init__(self, points, sides, rp = False):
        self.sides = sides
        self.rp = rp
        self.edge = self.calculate_edge(points)

        self.lines = self.calculate_lines()

    def calculate_edge(self, points):
        edges = []
        try:
            for i in range(0, len(points), 2):
                edges.append((Point(points[i], points[i+1])))
        except IndexError:
            pass
        if self.sides <= len(edges):
            return edges[0:self.sides]
        else:
            return edges

    def calculate_lines(self):
        lines = {}
        for r in range(len(self.edge)-1):
            lines[r] = [self.edge[r], self.edge[r+1]]
        lines[r+1] = [self.edge[r+1], self.edge[0]]

        return lines

    def draw(self, g):
        if len(self.edge) > 2 and self.sides > 2:
            if self.sides <= len(self.edge):
                for i in range(self.sides-1):
                    g.line(self.edge[i].x, self.edge[i].y, self.edge[i+1].x, self.edge[i+1].y)
                g.line(self.edge[0].x, self.edge[0].y, self.edge[i+1].x, self.edge[i+1].y)
            else:
                for i in range(len(self.edge)-1):
                    g.line(self.edge[i].x, self.edge[i].y, self.edge[i+1].x, self.edge[i+1].y)
                g.line(self.edge[0].x, self.edge[0].y, self.edge[i+1].x, self.edge[i+1].y)

            self.fill(g)



    def __limits(self, points):
        min_x, min_y = None,None
        max_x, max_y = None,None

        for p in points:
            if min_x is None:
                min_x, min_y = p.x, p.y
                max_x, max_y = p.x, p.y
            else:

                if min_x > p.x:
                    min_x = p.x

                if min_y > p.y:
                    min_y = p.y

                if max_x < p.x:
                    max_x = p.x

                if max_y < p.y:
                    max_y = p.y
        
        return Point(min_x, min_y), Point(max_x, max_y)

    def intersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        den = ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4))

        num_x = (x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)


        num_y = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)

        if den != 0:
            x, y = round(num_x/den), round(num_y/den)
            return Point(x, y)
        return None
    
    def sort_key(self, point):
        return (point.x, point.y)



    def fill(self, g):
        pattern = g.pattern
        if pattern == 1:
            self.fill_all(g, 1)

        if pattern == 2:
            self.fill_all(g, 17)

        if pattern == 3:
            self.v_lines(g, 17)

        if pattern == 4:
            self.fill_all(g, 17)
            self.v_lines(g, 17)

        if pattern == 5:
            self.d_main(g, 17)

        if pattern == 6:
            self.d_sec(g, 17)

        if pattern == 7:
            self.d_main(g, 17)
            self.d_sec(g, 17)


    def fill_all(self, g, h):
        p_min, p_max = self.__limits(self.edge)


        for l in range(0, (p_max.y-p_min.y), h):

            points = []
            inter = {}
            for key, value in self.lines.items():
                point = self.intersection(value[0].x, value[0].y, value[1].x, value[1].y, p_min.x, p_min.y+l, p_max.x, p_min.y+l)
                if point is not None:
                    inter[key] = point
            for key, value in inter.items():
                rg_mn, rg_mx = self.__limits([self.lines[key][0], self.lines[key][1]])
                if value.x in range(rg_mn.x, rg_mx.x+1) and value.y in range(rg_mn.y, rg_mx.y+1):
                    if self.rp:
                        if value not in points:
                            points.append(value)
                    else:
                        points.append(value)
            points = sorted(points, key = self.sort_key)
            self.draw_points(g, points)

    
    def v_lines(self, g, h):
        p_min, p_max = self.__limits(self.edge)

        for l in range(0, (p_max.x-p_min.x), h):

            points = []
            inter = {}
            for key, value in self.lines.items():
                point = self.intersection(value[0].x, value[0].y, value[1].x, value[1].y, p_min.x+l, p_min.y, p_min.x+l, p_max.y)
                if point is not None:
                    inter[key] = point
            for key, value in inter.items():
                rg_mn, rg_mx = self.__limits([self.lines[key][0], self.lines[key][1]])
                if value.x in range(rg_mn.x, rg_mx.x+1) and value.y in range(rg_mn.y, rg_mx.y+1):
                    if self.rp:
                        if value not in points:
                            points.append(value)
                    else:
                        points.append(value)

            points = sorted(points, key = self.sort_key)
 
            self.draw_points(g, points)


    
    def d_main(self, g, h):
        p_min, p_max = self.__limits(self.edge)

        start = p_min.x - (p_max.x - p_min.x)
        end = p_min.x
        for l in range(0, (p_max.x-p_min.x)*2, h):

            points = []
            inter = {}
            for key, value in self.lines.items():
                point = self.intersection(value[0].x, value[0].y, value[1].x, value[1].y, start+l, p_min.y, end+l, p_max.y)
                if point is not None:
                    inter[key] = point
            for key, value in inter.items():
                rg_mn, rg_mx = self.__limits([self.lines[key][0], self.lines[key][1]])
                if value.x in range(rg_mn.x, rg_mx.x+1) and value.y in range(rg_mn.y, rg_mx.y+1):
                    if self.rp:
                        if value not in points:
                            points.append(value)
                    else:
                        points.append(value)


            points = sorted(points, key = self.sort_key)
            self.draw_points(g, points)



    def d_sec(self, g, h):
        p_min, p_max = self.__limits(self.edge)

        start = p_max.x + (p_max.x - p_min.x)
        end = p_max.x
        for l in range(0, (p_max.x-p_min.x)*2, h):

            points = []
            inter = {}
            for key, value in self.lines.items():
                point = self.intersection(value[0].x, value[0].y, value[1].x, value[1].y, start-l, p_min.y, end-l, p_max.y)
                if point is not None:
                    inter[key] = point
            for key, value in inter.items():
                rg_mn, rg_mx = self.__limits([self.lines[key][0], self.lines[key][1]])
                if value.x in range(rg_mn.x, rg_mx.x+1) and value.y in range(rg_mn.y, rg_mx.y+1):
                    if self.rp:
                        if value not in points:
                            points.append(value)
                    else:
                        points.append(value)


            points = sorted(points, key = self.sort_key)
            self.draw_points(g, points)
            


    def draw_points(self, g, points):
        if len(points) % 2 == 0:
                for v in range(0,len(points),2):
                    g.line(points[v].x, points[v].y, points[v+1].x, points[v+1].y)
        elif len(points) > 1:
            tmp_point = points.pop()
            g.line(points[0].x, points[0].y, tmp_point.x, tmp_point.y)
        


    

class RegularP (IrregularP):
    def __init__(self, x_o, y_o, size, sides):
        self.x_o, self.y_o = x_o, y_o
        self.sides = sides
        self.size = size
        self.center = None
        self.points = []
        self.calculate_points()
        IrregularP.__init__(self, self.points, sides, rp = True)
    

    def calculate_points(self):
        angle = 360 / self.sides
        radius =  self.size / (2 * math.sin(math.radians(angle/2)))
        apothem =  self.size / (2 * math.tan(math.radians(angle/2)))
        self.center = Point(self.x_o + self.size/2, self.y_o - apothem)


        angle_vert = []
        for i in range(self.sides):
            angle_vert.append(round(angle * -i))


        for alpha in angle_vert:
            xx = round(radius * math.cos(math.radians(alpha)))
            yy = round(radius * math.sin(math.radians(alpha)))
            
            self.points.append(xx + round(self.center.x))
            self.points.append(yy + round(self.center.y))