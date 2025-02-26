class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=[]
        first_word = strs[0]
        min_len = min([len(word) for word in strs])
        for index, i in enumerate(first_word):
            if index >= min_len: 
                break
            result = all([word[index]==i for word in strs])
            if result:
                prefix.append(i)
            else: 
                break
        output = "".join(prefix)
        return output


            

            
            
        