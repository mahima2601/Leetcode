class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen=set()
        stack=[]
        last_index=dict()
        for i, ch in enumerate(s):
            last_index[ch] = i
        # for i in s:
        #     last_index[i]=s.index(i)
        print(last_index)

        for i, ch in enumerate(s):
            if ch in seen:
                continue 

            while stack and ch < stack[-1] and i < last_index[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            
            # add current char
            stack.append(ch)
            seen.add(ch)
            print(i, ch, stack)
        # 3. Convert stack to string
        return "".join(stack)
            
