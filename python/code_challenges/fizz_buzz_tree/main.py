from tree_fizz_buzz import TreeNode, fizz_buzz_tree


def main():
    # Create an example k-ary tree
    root = TreeNode(
        1,
        [
            TreeNode(3, [TreeNode(5), TreeNode(6)]),
            TreeNode(2, [TreeNode(9), TreeNode(10)]),
        ],
    )

    # Apply fizz_buzz_tree function
    new_root = fizz_buzz_tree(root)

    # Print original and modified trees
    print("Original tree:")
    print_tree(root)

    print("\nModified tree:")
    print_tree(new_root)


def print_tree(root):
    """
    Utility function to print a k-ary tree
    """
    if not root:
        return

    print(root.val)
    for child in root.children:
        print_tree(child)

        if __name__ == "__main__":
            main()

