def GeneratePosOrNegRandInt(minimum, maximum):
    """
    Generates a random value between two values. Specialty: these two values can range form negative to positive values.
    :param minimum: minimum number
    :param maximum: maximum number
    :return: A random integer value.
    """
    import random
    return round(minimum + (maximum - minimum) * random.random())