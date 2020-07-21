

def test_format_function():
    print("{}, {}!".format('Hello', 'World'))  # Hello, World!
    print("{0}, {1}!".format('Hello', 'World'))  # Hello, World!
    print("{1}, {0}!".format('Hello', 'World'))  # World, Hello!
    print('{2}, {1}, {0}'.format(*'abc'))


if __name__ == '__main__':
    test_format_function()
