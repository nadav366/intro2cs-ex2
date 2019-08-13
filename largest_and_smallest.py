
def largest_and_smallest(first, sec, third):
    """This function get three numbers  and returns the largest and smallest.
    :param first, sec, third: Numeric values to compare.
    :return: Numeric values of the largest and smallest.
    """
    # Search for the largest number
    if first > sec and first > third:
        big_est = first
    elif sec > third:
        big_est = sec
    else:
        big_est = third

    # Search for the smallest number
    if first < sec and first < third:
        smallest = first
    elif sec < third:
        smallest = sec
    else:
        smallest = third

    return big_est, smallest

