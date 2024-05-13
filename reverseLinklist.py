class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
current = head
for i in range(2, 6):
    current.next = Node(i)
    current = current.next

# Reverse the linked list
reversed_head = reverseLinkedList(head)

# Print the reversed linked list
current = reversed_head
while current:
    print(current.value, end=" ")
    current = current.next
