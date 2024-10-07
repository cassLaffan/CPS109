'''
This program will help us understand binary search!
Remember, binary search only really works on sorted data.
'''

# I like to think of binary search as finding the drain,
# then circling it.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right and result == -1:
        mid = (left + right) // 2 # Floor division
        if arr[mid] == target:
            result = mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50]
    target = 30
    print(binary_search(arr, target))  # Output: 2