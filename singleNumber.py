from typing import List
from functools import reduce


def singleNumber(nums: List[int]) -> int:
    '''
    result = nums[0]
    for index in range(1, len(nums)):
        result ^= nums[index]
    return result
    '''
    return reduce(lambda x, y: x ^ y, nums)


nums = [1, 1, 3, 2, 3]
result = singleNumber(nums)
print(result)

