class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1

        for j in dic:
            if dic[j]==1:
                # for k in s:
                if j in s:
                    return s.index(j)
        else:
            return -1


