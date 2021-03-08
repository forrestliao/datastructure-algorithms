# [1, -1, 2, 4, 1], Ans: 2
#［1, 2, 3, 4, 5, 6], Ans: 4
class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

def build_node_list(q):
    head = node = Node(q[0])
    for node_val in q[1:]:
        next_node = Node(node_val)
        node.next = next_node
        node = node.next
    return head

def one_pass_find_mid(head):
    res = None
    return res

def run_test():
    q = [1, -1, 2, 4, 1]
    ans = 2
    test(one_pass_find_mid(build_node_list(q)), ans)

    q = [1, 2, 3, 4, 5, 6]
    ans = 4
    test(one_pass_find_mid(build_node_list(q)), ans)

    # assume linked list = [], return None
    q = []
    ans = None
    test(one_pass_find_mid(build_node_list(q)), ans)

def test(res, ans):
    try:
        assert res == ans
        print("=== test pass ===")
    except AssertionError:
        print("=== test fail ===")

if __name__ == "__main__":
    run_test()