class Tree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(arr, i, node):
    if i < len(arr):
        node = Node(arr[i])
        node.left = insert(arr, 2 * i + 1, node.left)
        node.right = insert(arr, 2 * i + 2, node.right)
    return node


def balance(node):
    if node:
        left = 0 if node.left is None else node.left.value
        right = 0 if node.right is None else node.right.value
        node.value -= (left + right)
        balance(node.left)
        balance(node.right)


def post_order(node,alist):
    if node:
        post_order(node.left,alist)
        post_order(node.right,alist)
        alist.append(node.value)



if __name__ == '__main__':
    tree = Tree()
    arr = [25, 12, 9, 4, 3]
    tree.root = insert(arr, 0, tree.root)
    balance(tree.root)
    alist = []
    post_order(tree.root,alist)
    print(alist)