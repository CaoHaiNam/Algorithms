from typing import List
def canPartition(nums: List) -> bool:
    sum_all = sum(nums)
    if sum_all % 2 != 0:
        return False
    else:
        for i in range(len(nums)):
            current_sum = sum(nums[:i])
            # print(current_sum)
            for j in range(i, len(nums)):
                if 2*(current_sum + nums[j]) == sum_all:
                    return True
    return False

# print(canPartition([1,5,11,5]))
# print(canPartition([3,3,3,4,5]))
print(canPartition([1,2,3,4,5,6,7]))