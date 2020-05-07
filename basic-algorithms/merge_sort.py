"""
Merge Sort

Divide and conquer

Keep splitting list into half until down to groups of 1 element

"""


def mergesort(items):

    if len(items) <= 1:
        return items

    midpoint = len(items) // 2

    left = mergesort(items[:midpoint])
    right = mergesort(items[midpoint:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


# Test this out
merged = merge([1, 3, 7], [2, 5, 6])
print(merged)
