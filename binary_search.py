#Binary-Search

def binary_search(a_list, key):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if key < a_list[mid]:
            last = mid - 1
        elif key > a_list[mid]:
            first = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    assert(binary_search(test_list, 2) == 2)
    assert(binary_search(test_list, 20) == -1)
