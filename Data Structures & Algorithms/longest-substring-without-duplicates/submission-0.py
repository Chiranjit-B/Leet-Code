class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = set()
        l = 0
        ml = 0

        for r in range(len(s)) :
            while s[r] in subset :
                subset.remove(s[l])
                l+=1
            subset.add(s[r])
            ml = max(ml, r-l+1)
        return ml
