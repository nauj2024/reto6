class DatosInvalidosError(Exception):  # Excepcion personalizada para errores geometricos
    pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def compute_distance(self, sec):
        return ((self.x - sec.x)**2+(self.y - sec.y)**2)**(1/2)

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):  # Validación de tipo
            raise DatosInvalidosError("Los extremos deben ser objetos Point")
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def get_start_point(self):
        return self.start_point

    def set_start_point(self, new):
        self.start_point = new
        self.length = self.compute_length()

    def get_end_point(self):
        return self.end_point

    def set_end_point(self, new):
        self.end_point = new
        self.length = self.compute_length()

    def get_length(self):
        return self.length

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)

class Shape:
    def __init__(self, vertices: list, regular: bool = False):
        if len(vertices) < 3:  # Validación mínima de figura
            raise DatosInvalidosError("Una figura debe tener al menos 3 vertices")
        self.regular = regular
        self.vertices = vertices
        self.edges = self.compute_edges()
        self.angles = []

    def compute_edges(self):
        edges = []
        n = len(self.vertices)
        for i in range(n):
            edge = Line(self.vertices[i], self.vertices[(i+1)%n]) 
            edges.append(edge)
        return edges

    def get_regular(self):
        return self.regular

    def set_regular(self,new):
        self.vertices = new

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, new):
        self._vertices = new
        self._edges = self.compute_edges()

    def get_edges(self):
        return self.edges

    def get_angles(self):
        return self.angles

    def set_angles(self, new):
        self._inner_angles = new

    def compute_area(self):
        return None

    def compute_perimeter(self):
        return None

    def compute_inner_angles(self):
        return None

class Rectangle(Shape):
    def __init__(self, bottom_left: Point, width: float, height: float):
        if width <= 0 or height <= 0:  # Validación de lados positivos
            raise DatosInvalidosError("El ancho y el alto deben ser mayores que 0")
        self._width = width
        self._height = height
        vertices = [
            bottom_left,
            Point(bottom_left.get_x() + width, bottom_left.get_y()),
            Point(bottom_left.get_x() + width, bottom_left.get_y() + height),
            Point(bottom_left.get_x(), bottom_left.get_y() + height)
        ]
        super().__init__(vertices, regular=(width == height))

    def get_width(self):
        return self._width

    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value

    def compute_area(self):
        return self._width * self._height

    def compute_inner_angles(self):
        self.set_angles([90.0, 90.0, 90.0, 90.0])
        return self.get_angles()

class Square(Rectangle):
    def __init__(self, bottom_left: Point, side: float):
        if side <= 0:  # Validación de lado positivo
            raise DatosInvalidosError("El lado del cuadrado debe ser mayor que 0")
        super().__init__(bottom_left, side, side)

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        vertices = [p1, p2, p3]
        super().__init__(vertices)

    def compute_area(self):
        a = self.edges[0].get_length()
        b = self.edges[1].get_length()
        c = self.edges[2].get_length()
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5  

    def compute_inner_angles(self):
        return None

class Isosceles(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)

class Equilateral(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.set_angles([60.0, 60.0, 60.0])  

class Scalene(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)

class TriRectangle(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.set_angles([90.0, None, None])  
