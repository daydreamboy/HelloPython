# Usage:
# $ python3 07_argparse_optional_arguments_custom_action.py -i 42


import argparse


# Note: define a custom action which inherits from argparse.Actio
class VerboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('Here I am, setting the values %r for the %r option...' % (values, option_string))
        setattr(namespace, self.dest, values)


# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments with custom action
my_parser.add_argument('-i', '--input', action=VerboseStore, type=int)

# Execute the parse_args() method
args = my_parser.parse_args()

print(vars(args))
