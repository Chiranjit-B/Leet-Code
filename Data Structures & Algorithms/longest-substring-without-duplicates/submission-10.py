class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        maxL = 0
        dis = set()
        for r in range(len(s)) :
            while s[r] in dis :
                dis.remove(s[l])
                l+=1
            dis.add(s[r])

            maxL = max(maxL, r-l+1)
        return maxL


        