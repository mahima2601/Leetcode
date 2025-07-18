class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        self.left=left
        self.right=right
        var=0

        for i in range(self.left, (self.right)+1):
            var=var+self.nums[i]
        return var

            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)