from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        l= []

        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        return l
# nums = [1,2,5,2,3]
# target = 4
# targetIndices(nums, target)