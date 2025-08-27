class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_set=set(s)
        t_set=set(t)
        map_set=set()

        for i in range(len(s)):
            map_set.add((s[i], t[i]))

        if len(s_set)!=len(t_set):
            return False
        
        elif len(s_set)!=len(map_set):
            return False
        else:
            return True



        
            
