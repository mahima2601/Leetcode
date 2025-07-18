class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sort_l=sorted(nums, reverse=True)

        return (sort_l[0]-1)*(sort_l[1]-1)

        