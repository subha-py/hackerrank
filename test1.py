class Node:
    def __init__(self, value):
        self.value = value
        self.left_branch = None
        self.right_branch = None

    def __str__(self):
        return self.value


class Tree:
    def __init__(self, ):
        self.root = None


def insert(arr, root, i):
    if i < len(arr):
        root = Node(arr[i])
        root.left_branch = insert(arr, root.left_branch, 2 * i + 1)
        root.right_branch = insert(arr, root.right_branch, 2 * i + 2)
    return root


def preOrder(root):
    if root:
        left = root.left_branch
        right = root.right_branch
        left = 0 if left is None else left.value
        right = 0 if right is None else right.value
        root.value = root.value - (left + right)
        preOrder(root.left_branch)
        preOrder(root.right_branch)
        return root.value

def postOrder(root):
    if root:
        postOrder(root.left_branch)
        postOrder(root.right_branch)
        print(root.value)

if __name__ == '__main__':
    arr = [25, 12, 9, 4, 3]
    tree = Tree()
    tree.root = insert(arr, tree.root, 0)
    preOrder(root=tree.root)
    postOrder(root = tree.root)
