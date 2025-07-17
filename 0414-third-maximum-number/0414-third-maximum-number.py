class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums=set(nums)
        list_nums=list(set_nums)
        list_nums.sort(reverse=True)
        for i in range(len(list_nums)+1):
            if len(list_nums)>2:
                return (list_nums[2])
            else:
                return (list_nums[0])