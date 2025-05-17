# Example:
# binary_search([1, 3, 5, 7, 9], 7) → 3
# binary_search([1, 3, 5, 7, 9], 2) → -1


def binary_search(l, start, end, target):
    if start > end:  # Base case: element not found
        return -1
    mid = (start + end)//2
    # print(mid)

    if target < l[mid]:
        return binary_search(l, start, mid-1, target)
    elif target > l[mid]:
        return binary_search(l, mid+1, end, target)
    elif target == l[mid]:
        # return l.index(target)
        return mid
    else:
        return -1


lst = [1, 3, 5, 7, 9]
idx = binary_search(lst, 0, len(lst)-1, 9)
print(idx)






