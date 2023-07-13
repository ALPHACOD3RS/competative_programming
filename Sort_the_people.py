from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        k = [[names[i], heights[i]] for i in range(len(names))]
    

        for i in range(len(names)):
            for j in range(len(names)-1-i):
                if k[j][1] > k[j+1][1]:

                    k[j], k[j+1] = k[j+1], k[j]
        n = [k[i][0] for i in range( len(k))]
        return n[::-1]

    # print(k)


    

# names = ["Mary","John","Emma"]
# heights = [180,165,170]

# people(names, heights)
