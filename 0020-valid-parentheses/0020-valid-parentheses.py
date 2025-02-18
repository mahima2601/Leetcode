class Solution(object):
    def isValid(self, s):
        stack=[]
        mirror={")":"(", "}":"{","]":"["}
        for i in s:
            if i in {"(","{","["}:
                stack.append(i)
            else:
                if (len(stack)!=0) and mirror[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        