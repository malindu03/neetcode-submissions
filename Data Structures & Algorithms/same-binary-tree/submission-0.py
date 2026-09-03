# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q

        p_queue: deque[TreeNode | None] = deque([p])
        q_queue: deque[TreeNode | None] = deque([q])

        while p_queue and q_queue:
            p_level_size = len(p_queue)
            q_level_size = len(q_queue)

            # As we are doing BFS together they should both have the same level size
            for _ in range(p_level_size):
                p_node = p_queue.popleft()
                q_node = q_queue.popleft()

                if p_node is None and q_node is None:
                    continue
                p_val = None
                if p_node is not None:
                    p_val = p_node.val
                q_val = None
                if q_node is not None:
                    q_val = q_node.val

                if q_val != p_val:
                    return False
                
                if p_node.left:
                    p_queue.append(p_node.left)
                else:
                    p_queue.append(None)

                if q_node.left:
                    q_queue.append(q_node.left)
                else:
                    q_queue.append(None)

                if p_node.right:
                    p_queue.append(p_node.right)
                else:
                    p_queue.append(None)

                if q_node.right:
                    q_queue.append(q_node.right)
                else:
                    q_queue.append(None)


        return True