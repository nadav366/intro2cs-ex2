
def is_it_summer_yet(lim, a_temp, b_temp, c_temp):
    """ This function receives a desired temperature and checks whether
     in three days there were at least two days in which
      the temperature was a higher dimension
    :param lim: Numeric value, Temperature for comparison
    :param a_temp,  b_temp, c_temp: Numeric value temperature of three days
    :return: Boolean value True if it's summer and False else
    """
    if a_temp > lim:
        if b_temp > lim or c_temp > lim:
            return True
        else:
            return False
    if b_temp > lim and c_temp > lim:
        return True
    return False
