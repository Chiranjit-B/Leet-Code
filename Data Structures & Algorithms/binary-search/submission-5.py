class Solution:
    def search(self, nums: List[int], value: int) -> int:
        l = 0 
        r = len(nums)-1
        while l<=r :
            mid = int((l+r)/2)
            if value < nums[mid] :
                r = mid - 1
            elif value > nums[mid] :
                l = mid + 1
            else :
                return mid
        return -1
