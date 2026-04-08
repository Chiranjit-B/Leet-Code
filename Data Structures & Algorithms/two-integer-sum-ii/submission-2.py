class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int] :
        left = 0
        a = [] 
        right = len(nums)-1
        while left < right :
            if nums[left] + nums[right] > target :
                right-=1
            elif nums[left] + nums[right] < target :
                left+=1
            else :
                #flag+=1
                #a.append([nums[left],nums[right]])
                return ([left+1, right+1])
                if nums[left] == nums[left + 1] :
                    #a.append(nums[left], nums[right])
                    return ([left+1, right+1])
                    left+=1

                elif nums[right] == nums[right - 1] :
                    #a.append(nums[left], nums[right])
                    return ([left+1, right+1])
                    right-=1

                else :
                    left += 1
                    right -= 1 
        return a

                
                
                    





        
        