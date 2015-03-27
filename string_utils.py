def comma_and(iterable):
    if len(iterable) == 1:
        return iterable[0]
    if len(iterable) == 2:
        return "{0} and {1}".format(iterable[0], iterable[1])
    return ", ".join(iterable[:-1]) + ", and " + iterable[-1]

def s(number):
    if number == 1:
        return ""
    return "s"
