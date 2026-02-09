class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_nums1=sorted(nums1)
        new_nums2=sorted(nums2)
        j=i=0
        new=[]
        while i< len(new_nums1) and j< len(new_nums2):
            if new_nums1[i] == new_nums2[j]:
                new.append(new_nums1[i])
                i += 1
                j += 1
            elif new_nums1[i] < new_nums2[j]:
                i += 1
            else:
                j += 1

        return new


        