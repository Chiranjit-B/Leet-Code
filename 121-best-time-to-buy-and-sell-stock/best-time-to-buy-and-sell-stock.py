class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r =0,1
        maxP = 0
        pro = 0 
        while r < len(prices) :
            if prices[r] > prices[l] :
                pro = prices[r] - prices[l]
                maxP = max(maxP,pro)
            else :
                l = r
            r+=1
        return maxP
        