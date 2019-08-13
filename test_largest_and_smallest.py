import largest_and_smallest


def fun_four_tester():
    """ This function examines function 4, and prints the test result
    :return: Boolean value Has the test been successful
    """
    flag = True  # Boolean variable Which indicates whether the test failed
    # Some tests for possible input
    if largest_and_smallest.largest_and_smallest(1.5, 1.5, 1.5) != (1.5, 1.5):
        flag = False
    elif largest_and_smallest.largest_and_smallest(-10, -5, -15) != (-5, -15):
        flag = False
    elif largest_and_smallest.largest_and_smallest(1, 2.86, -4.89) != (2.86, -4.89):
        flag = False
    elif largest_and_smallest.largest_and_smallest(5, 14, 5) != (14, 5):
        flag = False
    elif largest_and_smallest.largest_and_smallest(2, 2, -3) != (2, -3):
        flag = False

    # Print the test result
    if flag:
        print("Function 4 test success")
    else:
        print("Function 4 test fail")
    return flag


if __name__ == "__main__":
    """ main function """
    fun_four_tester()
