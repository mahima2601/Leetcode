class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_length=0
        for i in range(0, k):
            max_length=max_length+nums[i]

        window=max_length

        for i in range(k, len(nums)):
            window=window+nums[i]-nums[i-k]
            max_length=max(max_length, window)

        return (max_length/k)

            
        