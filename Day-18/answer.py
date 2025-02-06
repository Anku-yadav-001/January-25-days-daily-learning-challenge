class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_linked_lists(head1, head2):
    carry = 0
    dummy = Node(0) 
    current = dummy

    while head1 or head2 or carry:
        val1 = head1.data if head1 else 0
        val2 = head2.data if head2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        digit = total % 10

        new_node = Node(digit)
        current.next = new_node
        current = new_node

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(' '.join(result))


t1 = int(input())
head1 = None
tail1 = None
for _ in range(t1):
    data = int(input())
    new_node = Node(data)
    if not head1:
        head1 = new_node
        tail1 = new_node
    else:
        tail1.next = new_node
        tail1 = new_node

t2 = int(input())
head2 = None
tail2 = None
for _ in range(t2):
    data = int(input())
    new_node = Node(data)
    if not head2:
        head2 = new_node
        tail2 = new_node
    else:
        tail2.next = new_node
        tail2 = new_node


result_head = add_linked_lists(head1, head2)

print_linked_list(result_head)