

# @see https://stackoverflow.com/questions/8930915/append-dictionary-to-a-dictionary/8930969#8930969
def add_dict_to_another_dict():
    d1 = {1: 1, 2: 2}
    d2 = {2: 'ha!', 3: 3}
    d1.update(d2)

    print(d1)


if __name__ == '__main__':
    add_dict_to_another_dict()
