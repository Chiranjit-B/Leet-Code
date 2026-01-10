class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP , p = 0, 0
        for r in  range(len(prices)) :
            if prices[r] > prices[l] :
                p = prices[r] - prices[l]
                maxP = max(maxP,p)
            else : 
                l = r
            
        return maxP

        