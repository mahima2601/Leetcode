class Solution(object):
    def romanToInt(self, s):
        range_values= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        total=0

        for index, a in enumerate(s):
            if index==(len(s)-1):
                total+=range_values[a]
            else:
                if range_values[a]>=range_values[s[index+1]]:
                    total+=range_values[a]
                else:
                    total-=range_values[a]
        return total
                





