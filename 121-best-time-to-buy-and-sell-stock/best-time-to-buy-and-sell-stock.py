class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        maxP = 0
        p = 0
        while r < len(prices) :
            if prices[r] > prices[l] :
                p = prices[r] - prices[l]
                maxP = max(maxP,p)
            else :
                l=r 
            r+=1
        return maxP
        