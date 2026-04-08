class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0   # buying price
        r = 1   # selling price 
        profit = 0
        while (r < len(prices)) :   # stopping on last possible selling date
            print(prices[l], prices[r])
            if prices[l] < prices[r] :  # profitability check 
                if prices[r] - prices[l] > profit : 
                    profit = prices[r] - prices[l]
                    
                
                 
            elif ((prices[r] < prices[l]) or (prices[r] == prices[l])):
                l  = r
            r += 1

        return profit 


                    