class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = list(s.lower())
        t = [char for char in t if char.isalnum()]

        print(t)



        left = 0
        flag = 0
        right = len(t) - 1 
        while left < right :
            if t[left] != t[right] :
                flag+=1
                break

            left+=1
            right-=1
        if flag > 0 :
            return False
        else :
            return True
        