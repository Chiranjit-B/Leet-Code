class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        ch = ""
        for i in range (len(s[0])) :
            for j in s :
                if i == len(j) or j[i] != s[0][i] :
                    return ch
            ch += s[0][i]
        return ch    