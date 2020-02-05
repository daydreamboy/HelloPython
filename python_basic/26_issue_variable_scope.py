
def method_with_issue(condition):
    if condition > 0:
        string = 'hello'

    string += ', world!'
    print(string)


# Error: UnboundLocalError: local variable 'string' referenced before assignment
# method_with_issue(0)

# Maybe Ok
# method_with_issue(1)


def method_with_fixed(condition):
    string = 'Hello'
    if condition > 0:
        string = 'hello'

    string += ', world!'
    print(string)


method_with_fixed(0)
method_with_fixed(1)



