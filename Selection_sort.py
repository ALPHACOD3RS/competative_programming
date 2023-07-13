def selection(nums : list[int]):
    for i in range(len(nums)):
        min = i

        for j in range(i+1, len(nums)):
            if nums[min] > nums[j]:
                # print(j)
                min = j

        nums[i], nums[min] = nums[min], nums[i]
#         print(nums)
#     print(nums)

# nums = [2, 4, 6 ,8, 3]
# selection(nums)