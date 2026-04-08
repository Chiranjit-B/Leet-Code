class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        p = 0
        max_p = 0
        for r in range(len(prices)) :
            if prices[r] > prices[l] : 
                p = prices[r] - prices[l]
                max_p = max(p,max_p)
            else :
                l = r                
            r+=1
        return max_p
