
def calculate_mathematical_expression(first_num, sec_num, act):
    """
    This function accepts two numbers and an action,
    and returns the result of the operation to both numbers
    :param first_num: First numeric value
    :param sec_num: secend numeric value
    :param act: A character representing an invoice action (+,-,*./)
    :return: numeric value the result of the operation
    """
    # Check which invoice action was accepted
    if act == '+':
        return first_num + sec_num
    if act == '-':
        return first_num - sec_num
    if act == '*':
        return first_num * sec_num
    if act == '/':
        if sec_num == 0:  # A test that is not divided by zero
            return None
        return first_num / sec_num
    return None  # Returns if an unknown action is received


def calculate_from_string(in_string):
    """ A function that calculates invoice operations
    :param in_string: string value of the account operation,separated by space
    :return: numeric value result of the action
    """
    div_list = in_string.split()  # Divide the string into a list
    # Distributing the list to variables
    first = float(div_list[0])
    second = float(div_list[2])
    act = div_list[1]
    # Returns the result of the action
    return calculate_mathematical_expression(first, second, act)


