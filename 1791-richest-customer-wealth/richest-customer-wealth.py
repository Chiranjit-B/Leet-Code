class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
       
        arr = []
        for a in accounts :
            arr.append(sum(a))
        #print(arr)
        return(max(arr))



        