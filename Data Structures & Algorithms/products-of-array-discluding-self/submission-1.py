class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #nums = [5,3,4,2]
        lp = [1]*len(nums)
        rp = [1]*len(nums)
        temp = 1
        lp[0] =  1
        for i in range(1, len(nums)) :
            lp[i]= nums[i-1]*temp
            temp   = lp[i]

        rp[len(nums)-1] = 1
        temp = 1
        length = len(nums)
        for i in range(length-1, 0,-1) :
            rp[i-1] = nums[i]*temp
            temp = rp[i-1]

       


        pro = [1]*length
        for i in range(length) :
            pro[i] = lp[i]*rp[i]

            
        #print(pro)

        return pro
        

        