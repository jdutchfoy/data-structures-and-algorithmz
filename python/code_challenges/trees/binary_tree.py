class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, node, result):
        if node:
            result.append(node.value)
            self.pre_order(node.left_child, result)
            self.pre_order(node.right_child, result)
        return result

    def in_order(self, node, result):
        if node:
            self.in_order(node.left_child, result)
            result.append(node.value)
            self.in_order(node.right_child, result)
        return result

    def post_order(self, node, result):
        if node:
            self.post_order(node.left_child, result)
            self.post_order(node.right_child, result)
            result.append(node.value)
        return result


class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left_child is None:
                        current.left_child = new_node
                        break
                    else:
                        current = current.left_child
                elif value > current.value:
                    if current.right_child is None:
                        current.right_child = new_node
                        break
                    else:
                        current = current.right_child

    def contains(self, value):
        current = self.root

        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left_child
            else:
                current = current.right_child

        return False
