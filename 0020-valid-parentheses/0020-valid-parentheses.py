class Solution:
    def isValid(self, s: str) -> bool:
        open=("(", "{", "[")
        close=(")", "}", "]")
        dic={"(": ")", "{": "}", "[": "]"}
        stack=[]
        for i in s:
            if i in open:
                stack.append(i)
            elif i in close:
                if not stack or dic[stack[-1]]!=i:
                    return False
                stack.pop()
            else:
             return False
        if stack:
            return False
        return True


        