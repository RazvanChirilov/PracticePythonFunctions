def divisible_by_10(nums):
    counter = 0
    for num in nums:
        if num % 10 == 0:
            counter += 1
    return counter

