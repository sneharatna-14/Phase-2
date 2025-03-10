def mergeIt(nums, left, mid, right):
# sorted array-1 would be from [left to mid]
# sorted array-2 would be from [mid + 1 to right]
 
    temp = []
    index1 = left 
    index2 = mid + 1 
 
    while index1<=mid and index2<=right:
        if nums[index1]<nums[index2]:
            temp.append(nums[index1])
            index1 += 1 
        else:
            temp.append(nums[index2])
            index2 += 1 
 
    while index1<= mid:
        temp.append(nums[index1])
        index1 += 1 

    while index2<= mid:
        temp.append(nums[index2])
        index2 += 1 
    index =left 

    for ele in temp:
        nums[index] = ele 
        index += 1
 
def divideAndMerge(nums, left, right):
    if left >= right:
        return
 
    mid = (left + right) // 2 
    divideAndMerge(nums, left, mid)
    divideAndMerge(nums, mid + 1, right)
    mergeIt(nums, left, mid, right)
 
 
def performMergeSort(nums):
    n = len(nums)
    divideAndMerge(nums, 0, n - 1)
 
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Before sorting:", nums)
 
performMergeSort(nums)
 
print("After sorting:", nums)
