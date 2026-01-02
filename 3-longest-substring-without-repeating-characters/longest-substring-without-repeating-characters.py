class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        sub = set()
        maxL = 0
        for r in range(len(s)) :
            while s[r] in sub :
                sub.remove(s[l]) 
                l+=1

            sub.add(s[r])
            maxL = max(maxL, r-l+1)
        return maxL

        