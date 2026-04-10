class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 
        maxP = 0
        while r < len(prices) :
            if prices[l] > prices[r] :
                l = r
            else :
                maxP = max((prices[r]-prices[l]), maxP)

            r+=1
        return maxP 