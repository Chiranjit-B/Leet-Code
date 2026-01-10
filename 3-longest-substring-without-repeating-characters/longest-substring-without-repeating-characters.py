class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        dup = set()
        maxL = 0
        for r  in range(len(s)) :
            while s[r] in dup :
                dup.remove(s[l])
                l+=1
            dup.add(s[r])
            maxL = max(maxL,r-l+1)
        return maxL

        