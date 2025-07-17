from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count=Counter(s)
        t_count=Counter(t)

        for i in t_count:
            if t_count[i]> s_count.get(i, 0):
                return i
                        