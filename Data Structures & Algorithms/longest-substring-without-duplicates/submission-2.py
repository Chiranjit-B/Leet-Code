class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        maxL = 0
        test = set()   # check for duplicate 
        for r in range(len(s)) :
            while s[r] in  test :
                test.remove(s[l])
                l+=1
            test.add(s[r])
            maxL= max(maxL, r-l+1)
        return maxL
            
        