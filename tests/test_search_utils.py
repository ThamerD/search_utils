import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.search_utils.search_utils import find_all

test_list = [1,2,3,1,5,6,1,1]

actual = find_all(test_list, 1)

expected = [1,1,1,1]

assert actual == expected
assert 1 == 1