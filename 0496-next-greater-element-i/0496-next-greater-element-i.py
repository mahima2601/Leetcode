class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        for i in nums1:
            nums2_i_index = nums2.index(i)
            found = False
            for j in range(nums2_i_index + 1, len(nums2)):
                if nums2[j] > i:
                    stack.append(nums2[j])
                    found = True
                    break
            if not found:
                stack.append(-1)

        return stack
