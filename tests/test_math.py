import equations.math_eq

def test_area_circle():
    assert equations.math_eq.Area_of_circle().area(5) == 78.53981634
    assert equations.math_eq.Area_of_circle().radius(76.5268) == 4.93550778

def test_area_triangle():
    assert equations.math_eq.Area_of_triangle().area(3, 5) == 7.5
    assert equations.math_eq.Area_of_triangle().base(3, 5) == 1.2
    assert equations.math_eq.Area_of_triangle().height(523.88456, 5) == 209.553824

def test_area_rectangle():
    assert equations.math_eq.Area_of_rectangle().area(532.5, 456) == 242820
    assert equations.math_eq.Area_of_rectangle().width(532.5,456) == 1.16776316
    assert equations.math_eq.Area_of_rectangle().width(532.5,52) == 10.24038462

def test_area_parallelogram():
    assert equations.math_eq.Area_of_rectangle().area(532.5, 456) == 242820
    assert equations.math_eq.Area_of_rectangle().width(532.5,456) == 1.16776316
    assert equations.math_eq.Area_of_rectangle().width(532.5,52) == 10.24038462

def test_area_trapezoid():
    assert equations.math_eq.Area_of_trapezoid().area(5, 8, 9) == 58.5
    assert equations.math_eq.Area_of_trapezoid().height(5, 8, 9) == 0.58823529
    assert equations.math_eq.Area_of_trapezoid().a(60, 5, 9) == 8.33333333
    assert equations.math_eq.Area_of_trapezoid().b(200, 2.2, 85) == 2.50588235

def test_area_ellipse():
    assert equations.math_eq.Area_of_ellipse().area(5,9) == 141.37166941
    assert equations.math_eq.Area_of_ellipse().a(956,9) == 33.81158347
    assert equations.math_eq.Area_of_ellipse().a(956,8) == 38.03803140
    
def test_area_ellipse():
    assert equations.math_eq.Area_of_sector().area(6,8) == 144
    assert equations.math_eq.Area_of_sector().radius(546,8) == 11.68332145
    assert equations.math_eq.Area_of_sector().theta(546,8) == 136.5
    