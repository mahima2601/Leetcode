class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <=k and m <=k:
            return 0
        elif n<=k or m>k:
            len1=m-k
            cost1=len1*k
            return cost1
        elif n>k or m<=k:
            len2=n-k
            cost2=len2*k
            return cost2

        