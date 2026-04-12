class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right :
            mid = int((left+right)/2)
            if target > arr[mid]:
                left = mid + 1
            elif target < arr[mid]:
                right = mid -1 
            else :
                return mid
        return -1
