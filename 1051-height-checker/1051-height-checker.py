class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sum=0
        expected=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                sum+=1
        return(sum)

        