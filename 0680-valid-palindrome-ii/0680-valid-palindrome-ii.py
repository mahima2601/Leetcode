class Solution(object):
    def validPalindrome(self, s):
        l=len(s)
        a=0
        b=l-1
        # counter = 0 
        while a<b :
            if s[a]==s[b]:
                a=a+1
                b=b-1
            else : 
                sub = s[a+1:b+1]
                if sub == sub[::-1]:
                    return True
                sub = s[a:b]
                if sub == sub[::-1]:
                    return True
                return False
        
        return True





        #     elif s[a]==s[b-1]:
        #         b=b-2
        #         a=a+1
        #         counter += 1
        #     elif s[b]==s[a+1]:
        #         a=a+2
        #         b=b-1
        #         counter += 1
        #     elif s[b]==s[a+1]:
        #         a=a+2
        #         b=b-1
        #         counter += 1
        #     else:
        #         return False

        # if counter==2:
        #     return False   
        # return True
                
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if s== (s[::-1]):
#             return True
# # s=mahima
# # a
# # idx=1
# # s[:1]+ s[2:]
#         else:
#             for idx, i in enumerate(s):
#                 # print(i)
#                 new_s=s[:idx]+  s[(idx+1):]
#                 # print(new_s)
#                 if new_s==(new_s[::-1]):
#                     return True
            
#         return False


        