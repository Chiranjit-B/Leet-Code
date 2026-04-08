class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        l = len(s)
        while i < len(s)/2 : 
            t      = s[l-i-1]
            s[l-i-1] = s[i]
            s[i]   = t
            i+=1
        return s