class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        d_s=deque()
        seen=set()
        l=0

        for i in s:
            if i not in seen:
                d_s.append(i)
                seen.add(i)
                l=max(l, len(seen))
            else:
                while i!=d_s[0]:
                    a=d_s.popleft()
                    seen.remove(a)
                
                d_s.popleft()
                d_s.append(i)
        return l








        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # final_max=0
        # final_set=set()
        # left=0
        # right=0
        # n=len(s)
        # while right<n:
        #     if s[right] not in final_set:
        #         final_set.add(s[right])
        #         final_max=max(final_max, len(final_set))
        #         right=right+1
        #     else:
        #         while s[left]!=s[right]:
        #             final_set.remove(s[left])
        #             left=left+1
        #         left=left+1
        #         right=right+1
        # return final_max





