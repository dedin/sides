# program to construct a binary
# search tree from a sorted array

class TreeNode:
    def __init__(self, nodevalue):
        self.val = nodevalue
        self.left = None
        self.right = None


def ArrtoBST(arr, start, end):
    if arr == None:
        return
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = ArrtoBST(arr, start, mid - 1)
    root.right = ArrtoBST(arr, mid+1, end)
    return root

def preOrder(root):
    if root == None:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root)
    inOrder(root.right)


def postOrder(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root)


def main():
    arr = [1,2,3,4,5,6,7]
    start = 0
    end = len(arr) - 1
    root = ArrtoBST(arr,start,end)
    preOrder(root)


if __name__ == "__main__":
    main()

