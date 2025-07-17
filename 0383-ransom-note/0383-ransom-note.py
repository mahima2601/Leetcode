from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)        # {'a': 2}
        magazine_counter = Counter(magazine)         # {'a': 2, 'b': 1}

        for i in ransom_counter:
            if ransom_counter[i] > magazine_counter[i]:
                return False
        return True

        