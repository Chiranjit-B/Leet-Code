class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for i in s :
            if (ord(i) >=97 and ord(i) <=122) or (ord(i) >=48 and ord(i) <=57) :
                arr.append(i)
        r = len(arr)-1
        l = 0
        while l < r :
            if arr[l] != arr[r] :
                return False
            l+=1
            r-=1
        return True   