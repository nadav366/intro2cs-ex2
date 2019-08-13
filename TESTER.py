import calculate_mathematical_expression
import largest_and_smallest
import convert_spoon_to_cup
import quadratic_equation
import test_largest_and_smallest


def convert_spoon_to_cup_test():
    flag = True
    if convert_spoon_to_cup.convert_spoon_to_cup(0) != 0:
        flag = False
    if convert_spoon_to_cup.convert_spoon_to_cup(16) != 1:
        flag = False
    if convert_spoon_to_cup.convert_spoon_to_cup(20) != 20 / 16:
        flag = False

    if flag:
        print("Function convert_spoon_to_cup test success")
    else:
        print("Function convert_spoon_to_cup test fail")


def calculate_mathematical_expression_test():
    flag = True

    if calculate_mathematical_expression.calculate_from_string("1 + 1") != 2:
       flag = False
    if calculate_mathematical_expression.calculate_from_string("5 + 7") != 12:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("2 * 9") != 18:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("34 a 12") != None:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("44 / 11.6") != 44 / 11.6:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("15 / 0") != None:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("34 - 12.7") != 34 - 12.7:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("15 & 1") != None:
        flag = False
    if calculate_mathematical_expression.calculate_from_string("15 * 0") != 0:
        flag = False

    if flag:
        print("Function calculate_mathematical_expression test success")
    else:
        print("***Function calculate_mathematical_expression test fail***")


def largest_and_smallest_test():
    flag = True

    if largest_and_smallest.largest_and_smallest(1, 1, 2) != (2, 1):
        flag = False
    if largest_and_smallest.largest_and_smallest(3, -6, 0) != (3, -6):
        flag = False
    if largest_and_smallest.largest_and_smallest(45,1,2) != (45, 1):
        flag = False
    if largest_and_smallest.largest_and_smallest(0, 0, 0) != (0, 0):
        flag = False
    if largest_and_smallest.largest_and_smallest(-78,1000,-56) != (1000, -78):
        flag = False
    if largest_and_smallest.largest_and_smallest(0,-1,0) != (0, -1):
        flag = False
    if largest_and_smallest.largest_and_smallest(1.5, 1.5, 1.5) != (1.5, 1.5):
        flag = False
    if largest_and_smallest.largest_and_smallest(-10, -5, -15) != (-5, -15):
        flag = False
    if largest_and_smallest.largest_and_smallest(1.98, 2.86, -4.895759) != (2.86, -4.895759):
        flag = False
    if largest_and_smallest.largest_and_smallest(5, 14, 5) != (14, 5):
        flag = False
    if largest_and_smallest.largest_and_smallest(2, 2, -3) != (2, -3):
        flag = False

    if flag:
        print("Function largest_and_smallest test success")
    else:
        print("Function largest_and_smallest test fail")


def quadratic_equation_test():
    flag = True


if __name__ == "__main__":
    """ main function """
    quadratic_equation.quadratic_equation_user_input()
    convert_spoon_to_cup_test()
    calculate_mathematical_expression_test()
    largest_and_smallest_test()
    test_largest_and_smallest.fun_four_tester()

