
def quadratic_equation(a, b, c):
    """ This function accepts factors of a second-order
    equation and returns the solutions
    :param a: Numeric value, factor of x^2, Suppose he did not 0
    :param b: Numeric value, factor of x
    :param c: Numeric value, free factor
    :return:  Numeric value, Equation solutions
    """
    delta = b ** 2 - 4 * a * c  # variable to the value within the root
    # Check out how many solutions there are
    if delta < 0:
        return None, None
    if delta == 0:
        return -b / (2 * a), None
    return (-b + (delta ** 0.5)) / (2 * a), (-b - (delta ** 0.5)) / (2 * a)


def quadratic_equation_user_input():
    """ This function accepts factors of a quadratic equation,
     separated by a space, and prints the solutions of the equation
    """
    str_input = input("Insert coefficients a, b, and c: ")
    list_input = str_input.split()  # split the input into list
    # split the list into variables
    a = float(list_input[0])
    b = float(list_input[1])
    c = float(list_input[2])
    sol1, sol2 = quadratic_equation(a, b, c)  # variable to the solutions
    # prints the solutions
    if sol1 is None:
        print("The equation has no solutions")
    elif sol2 is None:
        print("The equation has 1 solution: "+str(sol1))
    else:
        print("The equation has 2 solutions: "+str(sol1)+" and "+str(sol2))
    return

