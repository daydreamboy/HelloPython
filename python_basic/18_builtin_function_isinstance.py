import numbers


def check_object(a_object):
    print('------------------')
    print(a_object)
    print(f"is dict: {isinstance(a_object, dict)}")
    print(f"is list: {isinstance(a_object, list)}")
    # @see https://stackoverflow.com/questions/4187185/how-can-i-check-if-my-python-object-is-a-number
    # Warning: numbers.Number also includes True/False
    print(f"is Number: {isinstance(a_object, numbers.Number)}")
    print(f"is None: {a_object is None}")
    print(f"is bool: {isinstance(a_object, bool)}")


var = {}
check_object(var)

var = []
check_object(var)

var = 1
check_object(var)

var = 1.0
check_object(var)

var = 1j
check_object(var)

var = None
check_object(var)

var = False
check_object(var)

var = ()
check_object(var)


