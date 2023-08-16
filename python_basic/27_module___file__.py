import os


def test__file__():
    print(__file__)  # ./27_module__file__.py if python ./27_module__file__.py
    print(os.path.basename(__file__))  # 27_module__file__.py
    print(os.path.splitext(os.path.basename(__file__))[0])  # 27_module__file__


if __name__ == '__main__':
    test__file__()
