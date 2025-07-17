from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count=Counter(nums)
        for i in num_count:
            if num_count[i]>1:
                return True
        return False
        