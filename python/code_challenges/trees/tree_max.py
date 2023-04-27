class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root):
        self.root = BinaryTreeNode(root)
    
    def find_max_value(self):
        if self.root is None:
            return None
        
        max_val = self.root.data
        queue = [self.root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            
            if node.data > max_val:
                max_val = node.data
            
            if node.left is not None:
                queue.append(node.left)
                
            if node.right is not None:
                queue.append(node.right)
                
        return max_val
