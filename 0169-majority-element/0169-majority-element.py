class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = {}

        # Count occurrences
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

        # Find majority element
        for key, value in my_dict.items():
            if value > n // 2:
                return key
