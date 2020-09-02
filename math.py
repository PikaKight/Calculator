import math

class Area_of_circle:
    def area(self, r:float) -> float:
        self._area = math.pi*(r**2)
        return round(self._area, 8)

    def radius(self, A: float) -> float:
        self._radius = math.sqrt(A/math.pi) 
        return round(self._radius, 8)

class Area_of_triangle:
    def area(self, b:float, h:float) -> float:
        self._area = 0.5*b*h
        return round(self._area, 8)

    def base(self, A:float, h:float) -> float:
        self._base = (A*2) / h
        return round(self._base, 8)
    
    def height(self, A:float, b:float) -> float:
        self._height = (A*2) / b
        return round(self._height, 8)

class Area_of_rectangle:
    def area(self, l:float, w:float) -> float:
        self._area = l*w
        return round(self._area, 8)
    
    def length(self, A:float, w:float) -> float:
        self._length = A/w
        return round(self._length, 8)
    
    def width(self, A:float, l:float) -> float:
        self._width = A/l
        return round(self._width, 8)

class Area_of_parallelogram:
    def area(self, b:float, h:float) -> float:
        self._area = b*h
        return round(self._area, 8)
    
    def base(self, A:float, h:float) -> float:
        self._base = A/h
        return round(self._base, 8)
    
    def height(self, A:float, b:float) -> float:
        self._height = A/b
        return round(self._height, 8) 

class Area_of_trapezoid:
    def area(self, a:float, b:float, h:float) -> float:
        self._area = 0.5*(a+b)*h
        return round(self._area, 8)
    
    def height(self, A:float, a:float, b:float) -> float:
        self._height = (A*2) / (a+b)
        return round(self._height, 8)
    
    def a(self, A:float, b:float, h:float) -> float:
        self._a = ((A*2) / h) - b
        return round(self._a, 8)      
    
    def b(self, A:float, a:float, h:float) -> float:
        self._b = ((A*2) / h) - a
        return round(self._b, 8)  

class Area_of_ellipse:
    def area(self, a:float, b:float) -> float:
        self._area = math.pi*a*b
        return round(self._area, 8)

    def a(self, A:float, b:float) -> float:
        self._a = A/ (math.pi*b)
        return round(self._a, 8) 

    def b(self, A:float, a:float) -> float:
        self._b = A/ (math.pi*a)
        return round(self._b, 8)   

class Area_of_sector:     
    def area(self, r:float, theta:float) -> float:
        self._area = 0.5*(r**2)*theta
        return round(self._area, 8)

    def radius(self, A:float, theta:float) -> float:
        self._radius = math.sqrt((A*2)/theta)
        return round(self._radius, 8)
    
    def theta(self, A:float, r:float) -> float:
        self._theta = (A*2) / r
        return round(self._theta, 8)
