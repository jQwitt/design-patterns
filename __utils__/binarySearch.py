debug = False
sortedNums: list = [1, 2, 3, 4, 5, 6]

'''
    @return index of target
'''
def binSearch(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:

        mid = (left + right) // 2
        
        if debug:
            print('left: {}'.format(left))
            print('mid: {}'.format(mid))
            print('right: {}'.format(right))

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return -1

for n in sortedNums:
    print("passed" if binSearch(sortedNums, n) == sortedNums.index(n) else "failed")
for n in [-1, 100]:
    print("passed" if binSearch(sortedNums, n) == -1 else "failed")