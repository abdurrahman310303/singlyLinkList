# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_two_lists(l1, l2):
#     dummy = ListNode(0)
#     current = dummy

#     while l1 is not None and l2 is not None:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next

#     if l1 is not None:
#         current.next = l1
#     else:
#         current.next = l2

#     return dummy.next

# # Example usage
# # Constructing l1: 1 -> 3 -> 5 -> None
# l1 = ListNode(1)
# l1.next = ListNode(3)
# l1.next.next = ListNode(5)

# # Constructing l2: 2 -> 4 -> 6 -> None
# l2 = ListNode(2)
# l2.next = ListNode(4)
# l2.next.next = ListNode(6)

# merged_list = merge_two_lists(l1, l2)

# # Print the merged list
# while merged_list is not None:
#     print(merged_list.val, end=" ")
#     merged_list = merged_list.next
