def find_all(lst: list, k: object) -> list:
    '''
    Searches through given list and returns a list containing all elements that match the given search object.
    '''
    found = []
    for x in lst:
        if x == k:
            found.append(x)

    return found