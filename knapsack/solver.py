weights = [2,1,4,3]
values = [3,3,4,2]
max_weights = 6

# weights = [10, 3, 22, 50, 83, 16, 41]
# values = [99, 97, 54, 19, 50, 70, 48]
# max_weights = 22

def knapsack(weights, values, max_weights):
    result_table = [[0 for _ in range(max_weights+1)] for _ in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        w, v = weights[i-1], values[i-1]
        for j in range(1, max_weights+1):
            result_table[i][j] = result_table[i-1][j]
            # if w > j:
            #     result_table[i][j] = result_table[i-1][j]
            # else:
            if j >= w:
                result_table[i][j] = max(result_table[i-1][j], result_table[i-1][j - w] + v)
        #     print(result_table[i][j])
        # print(result_table)
    print(result_table)
    return
        
    
knapsack(weights, values, max_weights)