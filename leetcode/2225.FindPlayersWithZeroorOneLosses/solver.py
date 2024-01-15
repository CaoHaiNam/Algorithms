from collections import Counter
from typing import List

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    d_win = [i[0] for i in matches]
    d_lose = [i[1] for i in matches]

    c_win = Counter(d_win)
    c_lose = Counter(d_lose)

    w_res = []
    for i in c_win:
        if i not in c_lose:
            w_res.append(i)
    l_res = []
    for i in c_lose:
        if c_lose[i] == 1:
            l_res.append(i)
    return sorted(w_res), sorted(l_res)


matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]