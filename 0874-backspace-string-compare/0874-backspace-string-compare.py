class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a_stack=[]
        b_stack=[]

        for i in s:
            if i == "#":
                if a_stack:
                    a_stack.pop()
            else:
                a_stack.append(i)
        

        for j in t:
            if j == "#":
                if b_stack:
                    b_stack.pop()
            else:
                b_stack.append(j)

        if (''.join(a_stack)) == (''.join(b_stack)):
            return True
        else:
            return False