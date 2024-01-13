from collections import defaultdict, Counter
def minSteps(s: str, t: str) -> int:
    # if ''.join(sorted(list(s))) == ''.join(sorted(list(t))):
    #     return 0
    c1 = Counter(s)
    c2 = Counter(t)
    
    c3 = c1 - c2
    
    return sum(c3)

    