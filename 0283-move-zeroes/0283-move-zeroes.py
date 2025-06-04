class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i==0:
                zero_list=nums.remove(0)
                nums.append(0)
        return nums


        """
        Do not return anything, modify nums in-place instead.
        """
        