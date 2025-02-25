class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        max_list=[]
        curr_max = 0
        for i in prices[::-1]:
            if curr_max< i:
                max_list.append(i)
                curr_max=i
            else:
                max_list.append(curr_max)

        cmax = 0
        for i in range(n):
            cmax = max(cmax, max_list[n-1-i]-prices[i])
        return cmax

        








        # max_value=[]
        # for i in range (len(prices)):
        #     for j in range (i+1, len(prices)):
        #         if prices[i]< prices[j]:
        #             max_value.append(prices[j]-prices[i])
                
        # if max_value:
        #     return max(max_value)
        # else: 
        #     return 0
                
                    




        
        