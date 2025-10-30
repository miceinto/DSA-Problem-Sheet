class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    """
    Reverses a singly linked list.
    
    Args:
    head (ListNode): Head of the linked list
    
    Returns:
    ListNode: Head of the reversed list
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Time Complexity: O(n)
# Space Complexity: O(1)
