from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target :
                    return [i , j]
                # break  
        return [] 
    

# nums = [3,2,3]
# target = 6
# print(twoSum(nums, target))