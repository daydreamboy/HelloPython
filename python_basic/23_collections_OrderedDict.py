import collections
import json

var = {
    'c': "This is c",
    'a': "This is a",
    'd': "This is d",
    'b': "This is d"
}

a_list = sorted(var.items())
ordered_var = collections.OrderedDict(a_list)

print(json.dumps(ordered_var))


