import os
import sys


def assertFile(path):
    if not os.path.isfile(path):
        raise ValueError(f"{path} {'is a directory' if os.path.isdir(path) else 'doesn\'t exist'}.")



