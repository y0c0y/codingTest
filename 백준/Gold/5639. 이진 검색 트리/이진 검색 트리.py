import sys

sys.setrecursionlimit(10**6)


def postorder_from_preorder(preorder, start=0, end=None):
    if end is None:
        end = len(preorder)

    if start >= end:
        return []

    root = preorder[start]

    # Find the first element greater than the root.
    # This marks the start of the right subtree.
    i = start + 1
    while i < end and preorder[i] < root:
        i += 1

    # Recursively generate postorder sequence for left and right subtrees.
    left_postorder = postorder_from_preorder(preorder, start + 1, i)
    right_postorder = postorder_from_preorder(preorder, i, end)

    return left_postorder + right_postorder + [root]


number = []
while True:
    try:
        number.append(int(sys.stdin.readline()))
    except:
        break


result = postorder_from_preorder(number)
for node in result:
    print(node)
