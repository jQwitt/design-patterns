import random


nums = [9, 2, 4, 1, 8, 5, 3, 7, 0]

'''
  In place, recursive merge-sort
  @return sorted list
'''
def mergeSort(arr: list[int]) -> list[int]:
  length = len(arr)
  # break case, single element is sorted
  if length <= 1:
    return arr

  # divide into left and right sub arrays
  mid = length // 2
  L = arr[:mid]
  R = arr[mid:]

  # sort left and right sub arrays
  mergeSort(L)
  mergeSort(R)

  # merge sorted left and right sub arrays
  li, ri, ki = 0, 0, 0
  while li < len(L) and ri < len(R):
    if L[li] < R[ri]:
      arr[ki] = L[li]
      li += 1
    else:
      arr[ki] = R[ri]
      ri += 1
    ki += 1
  
  # append remaining elements
  while li < len(L):
    arr[ki] = L[li]
    ki += 1
    li += 1
  while ri < len(R):
    arr[ki] = R[ri]
    ki += 1
    ri += 1

for arr in [[random.randint(1,100) for i in range(100)] for n in range(10)]:
    sortedArr = sorted(arr)
    mergeSort(arr)
    print("passed" if arr == sortedArr else "failed")