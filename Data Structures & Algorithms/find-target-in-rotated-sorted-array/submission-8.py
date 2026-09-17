class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cut = getCut(nums, 0, n)
        if nums[cut] == target: return cut
        leftResult = binarySearch(nums, 0, cut, target)
        if leftResult != -1: return leftResult
        rightResult = binarySearch(nums, cut+1, n, target)
        if rightResult != -1: return rightResult
        return -1


def binarySearch(nums: List[int], start: int, end: int, key: int) -> int:
    if start >= end:
        return -1 
    pivot = start + (end - start) // 2
    if key == nums[pivot]: return pivot
    if key < nums[pivot]: return binarySearch(nums, start, pivot, key)
    else: return binarySearch(nums, pivot+1, end, key)
    
def getCut(nums: List[int], start: int, end: int) -> int:
    if start >= end:
        return -1
    pivot = start + (end - start) // 2
    if nums[pivot] <= nums[pivot-1]:
        return pivot 
    if nums[start] <= nums[start-1]:
        return start
    if nums[start] > nums[pivot]: # cut is in left-hand subarray
        return getCut(nums, start, pivot)
    else:
        return getCut(nums, pivot+1, end)