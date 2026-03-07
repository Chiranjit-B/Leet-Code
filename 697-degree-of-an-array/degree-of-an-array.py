class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = {}
        start = {}
        end = {}
        for i in range(len(nums)) :
            if nums[i] not in cnt :
                cnt[nums[i]] = 1
            else :
                cnt[nums[i]] += 1
            

            if nums[i] not in start :
                start[nums[i]] = i
                end[nums[i]]   = i
            else :
                end[nums[i]] = i

            
        degree = max(cnt.values())
        res = len(nums)
        for i in nums :
            if degree == cnt[i] :
                res = min(res, (end[i]-start[i]+1))
        return res
