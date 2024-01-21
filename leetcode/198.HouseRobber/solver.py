from typing import List

def rob(nums: List[int]) -> int:
    N = len(nums)
    res = [-1 for _ in range(N)]
    for i in range(N):
        if i == 0 or i == 1:
            res[i] = nums[i]
        else:
            res[i] = nums[i] + max(res[:i-1])
    return max(res)

nums = [2,7,9,3,1]
nums = [2,15,9,3,1]
print(rob(nums))