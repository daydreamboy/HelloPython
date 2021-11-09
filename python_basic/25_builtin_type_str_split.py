
if __name__ == '__main__':
    string = 'a b c'
    print(string.split())  # ['a', 'b', 'c']
    print(string.split(None))  # ['a', 'b', 'c']
    print(string.split(None, 1))  # ['a', 'b c']
    print('------------')

    string = 'a  b  c d'
    print(string.split())
    print(string.split(None, 1))
    print(string.split(None, 2))
    print(string.split(None, 3))
    print(string.split(None, 4))

