class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        s = s.lower()
        for i in s :
            if ((ord(i) >= 97 and ord(i) <= 122) or ( ord(i) >= 48 and ord(i) <=55  )) :
                arr.append(i) 

        l= 0 
        r = len(arr)-1
        while l < r :
            if arr[l] != arr[r] :
                return False
            l+=1
            r-=1
        return True
                       
        