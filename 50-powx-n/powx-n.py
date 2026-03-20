class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 1 :
            return x*pow(x,n-1)
        elif n < 0 :
            return (1/x)*pow(x,n+1)
        return 1

        