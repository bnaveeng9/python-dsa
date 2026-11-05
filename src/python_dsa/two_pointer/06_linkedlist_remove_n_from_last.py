"""
Remove N-th Node from End of Linked List
Problem
Given the head of a linked list and an integer n, remove the n-th node from the end of the list and return the head of the modified list.

Input:

head: the head node of a singly linked list
n: an integer representing the position from the end (1-indexed)
Output:

Return the head of the modified linked list
Constraints:

The list has at least 1 node
n is a valid position from the end (1 <= n <= length of list)
Examples:

Example 1:


Copy
Input: head = [1, 2, 3, 4], n = 1
Output: [1, 2, 3]
Explanation: Remove the 1st node from the end (value 4)
Example 2:


Copy
Input: head = [1, 2, 3, 4], n = 2
Output: [1, 2, 4]
Explanation: Remove the 2nd node from the end (value 3)
Example 3:


Copy
Input: head = [1, 2, 3, 4], n = 4
Output: [2, 3, 4]
Explanation: Remove the 4th node from the end (the head, value 1)

"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy
    
    for x in range(n):
        if fast.next is None:
            return head 
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
            
    slow.next = slow.next.next
    return dummy.next
        
    

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None:
        return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    n = int(input())
    res = remove_nth_from_end(head, n)

    print(" ".join(format_list(res)))
