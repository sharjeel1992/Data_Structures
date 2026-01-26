"""
Binary Tree Traversals (DFS + BFS)

Run this file to see outputs printed in the terminal.

Covers:
- Building a binary tree
- DFS traversals (preorder, inorder, postorder)
  - Recursive implementations
  - Iterative implementations using a stack
- BFS (level-order traversal) using a queue (deque)
"""

from collections import deque


class TreeNode:
    """A single node in a binary tree."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_sample_tree():
    """
    Builds and returns the following tree:

            1
    #    /   \
         2     3
          \   / \
           6 4   5

    Returns:
        TreeNode: root of the tree
    """
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(4)
    d = TreeNode(5)
    e = TreeNode(6)

    root.left = a
    root.right = b
    a.right = e
    b.left = c
    b.right = d

    return root


# -------------------- DFS (Recursive) --------------------

def preorder_recursive(root):
    """Preorder DFS (Root, Left, Right) - recursive."""
    res = []

    def dfs(node):
        if node is None:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


def inorder_recursive(root):
    """Inorder DFS (Left, Root, Right) - recursive."""
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


def postorder_recursive(root):
    """Postorder DFS (Left, Right, Root) - recursive."""
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res


# -------------------- DFS (Iterative with Stack) --------------------

def preorder_iterative(root):
    """Preorder DFS (Root, Left, Right) - iterative using a stack."""
    if root is None:
        return []

    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        res.append(node.val)

        # Push right first so left is processed first
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return res


def inorder_iterative(root):
    """Inorder DFS (Left, Root, Right) - iterative using a stack."""
    res = []
    stack = []
    cur = root

    while cur is not None or stack:
        # Go as far left as possible
        while cur is not None:
            stack.append(cur)
            cur = cur.left

        # Visit
        cur = stack.pop()
        res.append(cur.val)

        # Then go right
        cur = cur.right

    return res


def postorder_iterative(root):
    """
    Postorder DFS (Left, Right, Root) - iterative using TWO stacks.
    (This approach is easier to understand than the one-stack variant.)
    """
    if root is None:
        return []

    s1 = [root]
    s2 = []
    res = []

    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left is not None:
            s1.append(node.left)
        if node.right is not None:
            s1.append(node.right)

    while s2:
        res.append(s2.pop().val)

    return res


# -------------------- BFS (Level-Order using Queue) --------------------

def level_order_bfs(root):
    """
    BFS level-order traversal using a queue.
    Returns a list of levels, e.g. [[1], [2,3], [4,5]]
    """
    if root is None:
        return []

    res = []
    q = deque([root])

    while q:
        level_size = len(q)  # number of nodes in the current level
        level = []

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

        res.append(level)

    return res


if __name__ == "__main__":
    root = build_sample_tree()

    print("Tree Traversals Demo\n")

    print("Preorder (recursive): ", preorder_recursive(root))
    print("Inorder (recursive):  ", inorder_recursive(root))
    print("Postorder (recursive):", postorder_recursive(root))
    print()

    print("Preorder (iterative): ", preorder_iterative(root))
    print("Inorder (iterative):  ", inorder_iterative(root))
    print("Postorder (iterative):", postorder_iterative(root))
    print()

    print("BFS level-order:      ", level_order_bfs(root))
