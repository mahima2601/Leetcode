class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0  # Slow pointer
        for j in range(1, len(nums)):  # Fast pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1  # Number of unique elements