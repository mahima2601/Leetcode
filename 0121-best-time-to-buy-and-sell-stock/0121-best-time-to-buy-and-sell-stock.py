class Solution(object):
    def maxProfit(self, prices):
        curr_max = 0 
        l = 0 
        r = 1
        n = len(prices)
        while r<n:
            if prices[l]<prices[r]:
                curr_max = max(curr_max, prices[r]-prices[l])
                r +=1
            else:
                l = r
                r = l+1
        return curr_max

            





        # if not prices:
        #     return 0
        # n = len(prices)
        # max_list=[]
        # curr_max = 0
        # for i in prices[::-1]:

        #     if curr_max< i:
        #         max_list.append(i)
        #         curr_max=i
        #     else:
        #         max_list.append(curr_max)

        # cmax = 0
        # for i in range(n):
        #     cmax = max(cmax, max_list[n-1-i]-prices[i])
        # return cmax

        








        # max_value=[]
        # for i in range (len(prices)):
        #     for j in range (i+1, len(prices)):
        #         if prices[i]< prices[j]:
        #             max_value.append(prices[j]-prices[i])
                
        # if max_value:
        #     return max(max_value)
        # else: 
        #     return 0
                
                    




        
        