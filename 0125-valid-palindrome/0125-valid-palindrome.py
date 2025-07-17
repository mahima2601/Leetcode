class Solution:
    def isPalindrome(self, s: str) -> bool:
        from collections import deque
        new_str=[]
        for i in s:
            if i.isalnum():
                new_str.append(i.lower())
        cleaned=''.join(new_str)
        d_str=deque(new_str)

        while len(d_str)>1:
            if d_str.pop() != d_str.popleft():
                return False
        return True