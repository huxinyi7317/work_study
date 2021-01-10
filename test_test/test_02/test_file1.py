import os
import sys
path = os.path.abspath(r'.')
sys.path.append(path)
path = sys.path
print(path)
from test_test.test_01.test_file import test_fcuntion


test_fcuntion()