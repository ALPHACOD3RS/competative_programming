class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        y = 0
        for i in range(len(nums)):
           if y in nums:
               pass
           else:
               print(i)
               break
           y+=1

        return y

