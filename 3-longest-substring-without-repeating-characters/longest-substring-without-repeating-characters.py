class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0 # 2 pointers for sliding window
        ch = set() # character set to check duplicate character
        maxL = 0 # variable to keep track the length of the characters
        while r < len(s) :
            while s[r] in ch :
                ch.remove(s[l])
                l+=1
            ch.add(s[r])
            maxL = max(maxL,r-l+1)
            r+=1
        return maxL
