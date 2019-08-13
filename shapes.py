import math


def circle_area():
    """ This function receives a numerical input for the radius
     of the circle and returns its area
    :return: Numeric value the circle area
    """
    radios = float(input())
    return math.pi * (radios ** 2)


def rectangle_area():
    """ This function receives two numerical inputs for the
    rectangle sides and returns its area
    :return: Numeric value the rectangle area
    """
    a_side = float(input())
    b_side = float(input())
    return a_side * b_side


def trapezoid_area():
    """ This function receives a numerical input for the
    Sides of the triangle and returns its area
    :return: Numeric value the triangle area
    """
    adage = float(input())
    return ((3 ** 0.5) / 4) * (adage ** 2)


def shape_area():
    """ This function is accepted as input to which shape
    the area should be calculated
       :return: Numeric value the shape area
       """
    choose = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if choose == '1':
        return circle_area()
    elif choose == '2':
        return rectangle_area()
    elif choose == '3':
        return trapezoid_area()
    else:
        return None

