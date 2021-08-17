def max_num(nums):
    greater_number = nums[0]
    for num in nums:
        if num > greater_number:
            greater_number = num
    return greater_number


print(max_num([75, 50, -10, 0, 20]))