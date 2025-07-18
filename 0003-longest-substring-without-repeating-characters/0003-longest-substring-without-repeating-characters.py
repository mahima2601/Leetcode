class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final_max=0
        final_set=set()
        left=0
        right=0
        n=len(s)
        while right<n:
            if s[right] not in final_set:
                final_set.add(s[right])
                final_max=max(final_max, len(final_set))
                right=right+1
            else:
                while s[left]!=s[right]:
                    final_set.remove(s[left])
                    left=left+1
                left=left+1
                right=right+1
        return final_max





