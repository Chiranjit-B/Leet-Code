class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        maxP, p = 0, 0
        for r in range (len(prices)) :
            if prices[r] > prices[l] :
                p = prices[r] - prices[l]
            else :
                l = r
            maxP = max(maxP,p)
        return maxP

        
        