import os

import resources


def abs_path(file):
    return os.path.abspath(os.path.join(os.path.dirname(resources.__file__), file))
