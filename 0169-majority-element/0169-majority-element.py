class Solution(object):
    def majorityElement(self, nums):
        element={}
        for i in nums:
            if i not in element:
                element[i]=1
            else:
                element[i]= element[i]+1
        for i in element:
            if element[i]>(len(nums)/2):
                return i


        