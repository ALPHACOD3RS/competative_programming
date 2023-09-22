class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         b = []
         for i in range(len(nums)):
             a = 0
             for j in range(len(nums)):
                 if nums[j] < nums[i]:
                     a+=1
             b.append(a)
         return(b)