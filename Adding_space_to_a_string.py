from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        stri = ""
        p = 0

        for x in spaces:
            # print((s[p:x]+ ' '))

            stri+=(s[p:x] + ' ')
            p = x

        stri+=(s[p:])

        # print(stri)
        return stri


"""
Test case

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
addSpace(s, spaces)


"""


