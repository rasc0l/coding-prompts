class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Use the fact that you can concatenate the lists to make the lists
# of equal length, then it is possible to find the repeating sublist
# by just walking through the concatenated lists
def findIntersect(a: ListNode, b: ListNode) -> ListNode:
    currA = a
    currB = b
    while currA is not currB:
        if currA.next is None:
            currA = b
        else:
            currA = currA.next
        if currB.next is None:
            currB = a
        else:
            currB = currB.next
    return currA

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