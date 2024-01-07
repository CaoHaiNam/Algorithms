nums_list = [
    [1,3,5,9,13],
    [2,4,6,8,10],
    [7,7,7,7,7]
]

def numOfArithmeticSlices(nums):
    L = [[] for _ in range(len(nums))]
    for i, num in enumerate(nums):
        if i == 0:
            continue
        elif i == 1:
            diff = num - nums[0]
            l = 1
            L[i].append([diff, l])
        else:
            for j in range(i):
                diff = num - nums[j]
                print(diff)
                print(L[j])
                for x in L[j]:
                    diff_ = x[0]
                    l_ = x[1]
                    if diff == diff_:
                        L[j].append([diff, l_+1])
                    else:
                        L[j].append([diff, 1])
    
    return L

for nums in nums_list:
    print(numOfArithmeticSlices(nums))
    break