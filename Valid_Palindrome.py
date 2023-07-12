class Solution:
    def isPalindrome(self, s: str) -> bool:
       s = ''.join(x.lower() for x in s if x.isalpha())
    #    print(s)

       return s == s[::-1]
# s = "race a car"
# print(Solution().isPalindrome(s))