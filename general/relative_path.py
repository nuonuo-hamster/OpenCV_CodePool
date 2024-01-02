import os
import sys

def relative_path():

    # ..\\general
    dirname = os.path.dirname(__file__)
    # ..\\general\\relative\\path\\to\\file\\you\\want
    filename = os.path.join(dirname, 'relative\\path\\to\\file\\you\\want')

    sys.path.append(os.getcwd())
    print(sys.path)

    return os.getcwd()

# relative_path()