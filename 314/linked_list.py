class ListNode:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.next = None
        
def findIntersect(a: ListNode, b: ListNode) -> ListNode:
    while a is not None:
        a.visited = True
        a = a.next
    while b is not None:
        if b.visited:
            return b
        else:
            b = b.next
    return None

a_node_one = ListNode(1)
a_node_two = ListNode(2)
b_node_one = ListNode(5)
b_node_two = ListNode(12)
b_node_three = ListNode(4)
shared_node_one = ListNode(84)
shared_node_two = ListNode(100)

a_node_one.next = a_node_two
a_node_two.next = shared_node_one
b_node_one.next = b_node_two
b_node_two.next = b_node_three
b_node_three.next = shared_node_one
shared_node_one.next = shared_node_two

print(findIntersect(a_node_one, b_node_one) == shared_node_one)