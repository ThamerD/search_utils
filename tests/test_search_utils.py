from search_utils.search_utils import find_all

def test_find_all():
    test_list = [1,2,3,1,5,6,1,1]

    actual = find_all(test_list, 1)

    expected = [1,1,1,1]

    assert actual == expected, f"Expected {expected}, but got {actual}"