class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for i in range(len(s)):
            if (ord(s[i]) <= 122  and ord(s[i]) >=97 ) or (ord(s[i])>= 48 and ord(s[i])<= 57)  :
                arr.append(s[i])
        print(arr)
        l = 0
        r = len(arr)-1
       
        while l < r :
            if arr[l] == arr[r] :
                l+=1
                r-=1
            else :
                return False
        return True
                

        