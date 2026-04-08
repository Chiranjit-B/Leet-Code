class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        max_profit = 0
        while (r < len(prices)) :
            # print(max_profit)
            if prices[l]<prices[r] :
                if max_profit < (prices[r]-prices[l]) :
                    max_profit = prices[r]-prices[l]
               
                   
         
            else : 
                l=r
            r+=1
            # print(prices[l])
            # print(prices[r]) 




            #l = r   
            #r+=1        
        return max_profit






                    