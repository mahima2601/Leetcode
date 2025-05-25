class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                prev = stack[-1]
                # Check if current and previous are consecutive (considering 'a' and 'z')
                if (ord(char) - ord(prev)) % 26 == 1 or (ord(prev) - ord(char)) % 26 == 1:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return ''.join(stack)