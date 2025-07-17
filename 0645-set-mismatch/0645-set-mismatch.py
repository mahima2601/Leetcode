from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing=-1
        duplicate=-1
        count_nums=Counter(nums)

        for i in range(1, len(nums)+1):

            if count_nums[i]==2:
                duplicate=i
            elif count_nums[i]==0:
                missing=i
                

        return [duplicate,missing]
            



        