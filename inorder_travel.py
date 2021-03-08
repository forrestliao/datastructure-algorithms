class TreeNode:
    def __init__(self, root = None):
        self.val = root
        self.left = None
        self.right = None

def build_tree(node_list= [1, 2, 3, 4, 5, 6, 7]):

    def insert(node_list, root, i, n):
        if i<n:
            root = TreeNode(node_list[i])

            # insert left child
            root.left = insert(node_list, root.left, 2 * i + 1, n)
            # insert right child
            root.right = insert(node_list, root.right, 2 * i + 2, n)
        return root

    n = len(node_list)
    root = None
    root = insert(node_list, root, 0, n)

    return root

def inorder_recursive(node):
    inorder_res = []
    def inorder_travel(node):
        if node != None:
            if node.left != None:
                inorder_travel(node.left)
            if node.val:
                inorder_res.append(node.val)
            if node.right != None:
                inorder_travel(node.right)

    inorder_travel(node)
    return inorder_res

def inorder_iteration(node):
    inorder_res = []
    stack = []
    while node or stack!= []:
        # if not left, pop the top node, and set current to top node's right node
        if node!= None:
            stack.append(node)
            node =  node.left
        elif node == None and stack!= []:
            poped_node = stack.pop()
            if poped_node.val!= None:
                inorder_res.append(poped_node.val)
                node = poped_node.right
    return inorder_res

def run_test():
    """
         1
        /  \
       2    3
      /\   / \
     4  5 6   7
    inorder: 4 2 5 1 6 3 7
    """
    tree = build_tree([1, 2, 3, 4, 5, 6, 7])
    ans = [4, 2, 5, 1, 6, 3, 7]
    inorder_recursive_res = inorder_recursive(tree)
    test(inorder_recursive_res, ans)
    inorder_iteration_res = inorder_iteration(tree)
    test(inorder_iteration_res, ans)

    """
         1
        / \
       2   3
      /\
     4  5
    inorder: 4 2 5 1 3
    """
    tree = build_tree([1, 2, 3, 4, 5])
    ans = [4, 2, 5, 1, 3]
    inorder_recursive_res = inorder_recursive(tree)
    test(inorder_recursive_res, ans)
    inorder_iteration_res = inorder_iteration(tree)
    test(inorder_iteration_res, ans)

    """
         1
        /
       2
      /\
     4  5
    inorder: 4 2 5 1 3
    """
    tree = build_tree([1, 2, None, 4, 5])
    ans = [4, 2, 5, 1]
    inorder_recursive_res = inorder_recursive(tree)
    test(inorder_recursive_res, ans)
    inorder_iteration_res = inorder_iteration(tree)
    test(inorder_iteration_res, ans)


def test(res, ans):
    try:
        assert res == ans
        print("=== test pass ===")
    except AssertionError:
        print("=== test fail ===")

if __name__ == "__main__":
    run_test()
