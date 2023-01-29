import os

from demoqa_tests import utils


def path(file):
    return os.path.abspath(
        os.path.join(os.path.dirname(utils.__file__), f'../../resources/{file}')
    )
