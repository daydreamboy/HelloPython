# import inspect
# import os
# import sys
#
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

# hack sys.path, https://stackoverflow.com/a/11158224

import dump_tool2

if __name__ == '__main__':
    spam = 45
    dump_tool2.dump_object(spam)

