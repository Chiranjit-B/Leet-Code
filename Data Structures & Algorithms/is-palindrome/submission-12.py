class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr= []
        for i in s :
            if (ord(i) >=97 and ord(i)<=122) or (ord(i) >= 48 and ord(i) <= 57) :
                arr.append(i)

        for i in range(len(arr)) :
            if arr[i] != arr[len(arr)-i-1] :
                return False
        return True

        