class Solution(object):
    def isPalindrome(self, s):
        s_clean= "".join(char for char in s if char.isalnum())
        if (s_clean.lower())==(s_clean[::-1].lower()):
            return True
        else:
            return False
        