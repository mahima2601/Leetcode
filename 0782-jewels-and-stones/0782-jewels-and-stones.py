class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dic={}
        count=0
        for i in stones:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for j in jewels:
            if j in dic.keys():
                count=count+(dic[j])
        return count

            