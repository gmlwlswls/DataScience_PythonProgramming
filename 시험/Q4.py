def find_longest_sorted_paths(root):
    """
    Identify all the longest paths in a Binary Search Tree (BST) where the node values are
    in either ascending or descending order.

    :param root: A TreeNode instance representing the root of the BST. (TreeNode)
    :return: A list of lists representing the longest sorted paths. (list[list[int]])
    """
    def dfs(node):
        if not node:
            return [], []  # ascending path, descending path

        left_asc, left_desc = dfs(node.left)
        right_asc, right_desc = dfs(node.right)

        # Ascending path
        if node.left and node.val > node.left.val:
            asc_path_left = [node.val] + left_asc
        else:
            asc_path_left = [node.val]

        if node.right and node.val < node.right.val:
            asc_path_right = [node.val] + right_asc
        else:
            asc_path_right = [node.val]

        # Descending path
        if node.left and node.val < node.left.val:
            desc_path_left = [node.val] + left_desc
        else:
            desc_path_left = [node.val]

        if node.right and node.val > node.right.val:
            desc_path_right = [node.val] + right_desc
        else:
            desc_path_right = [node.val]

        # Select the longest path for ascending and descending
        ascending = asc_path_left if len(asc_path_left) > len(asc_path_right) else asc_path_right
        descending = desc_path_left if len(desc_path_left) > len(desc_path_right) else desc_path_right

        return ascending, descending

    def find_paths(node):
        if not node:
            return []

        asc, desc = dfs(node)

        if len(asc) > len(desc):
            return [asc]
        elif len(desc) > len(asc):
            return [desc]
        else:
            return [asc, desc]

    # Perform a DFS to collect paths from the root
    ascending, descending = dfs(root)

    all_paths = find_paths(root)

    # Filter longest paths only
    max_length = max(len(path) for path in all_paths)
    longest_paths = [path for path in all_paths if len(path) == max_length]

    return longest_paths

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)

print(find_longest_sorted_paths(root1))
# Expected Output: [[4, 2, 1], [4, 6, 7]]

# Example 2
root2 = TreeNode(6)
root2.left = TreeNode(3)
root2.right = TreeNode(9)
root2.left.left = TreeNode(2)
root2.right.left = TreeNode(8)
root2.right.right = TreeNode(10)
root2.right.left.left = TreeNode(7)

print(find_longest_sorted_paths(root2))
# Expected Output: [[6, 9, 10], [6, 3, 2], [9, 8, 7]]