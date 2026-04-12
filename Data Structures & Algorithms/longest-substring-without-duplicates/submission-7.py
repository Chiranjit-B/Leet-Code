class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        maxL = 0
        res = set()
        for r in range (len(s)) :
            while s[r] in res :
                print("check")
                res.remove(s[l])
                l+=1
            res.add(s[r])
            maxL = max(maxL, r-l+1)
        print("test")
        return maxL
        