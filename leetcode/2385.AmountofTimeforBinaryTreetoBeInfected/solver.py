# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def amountOfTime(root: Optional[TreeNode], start: int) -> int:
    if not root:
        return 0
    
    # create a set to track infected node and a queue for BFS
    infected_node = set([start])
    queue = deque([(start, 0)])
        
    while queue:
        node, time = queue.popleft()
        
        if node and node.left.val not in infected_node:
            infected_node.add(node.left.val)
            queue.append((node.left.val, time+1))
            
        if node and node.right.val not in infected_node:
            infected_node.add(node.right.val)
            queue.append((node.right.val, time+1))
            
    return time


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

start_node = root.left.val  # Start infection from node with value 2
# print(start_node.val)

result = amountOfTime(root, start_node)
print("Minutes needed for the entire tree to be infected:", result)      
        
        