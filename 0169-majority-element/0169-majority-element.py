class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num="none"
        count=0
        for i in nums:
            if count==0:
                num=i
            if num==i:
                count=count+1
            else:
                count=count-1
        return num



























        # n=len(nums)
        # new_n=n/2
        # count_list={}
        # for i in nums:
        #     count_list[i]=nums.count(i)
        # for num, count in count_list.items():
        #     if count>new_n:
        #         return num
