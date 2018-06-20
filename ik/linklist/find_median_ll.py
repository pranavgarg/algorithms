#!/bin/python3
'''
Find Median Of Sorted Circular Singly Linked List


Problem Statement:

Given a pointer ptr to an arbitrary node of a sorted circular singly linked list L containing only even integers. You have to find the median value M of L.

When even number of elements in L, then the median M is average of two middle elements.

Input Format:

There is only one argument, ptr denoting a pointer to an arbitrary node of L.

Output Format:

Return one integer denoting the median M.

Constraints:

1 <= Number of nodes in linked list <= 10^5
- 2 * 10^9 <= value contained in nodes <= 2 * 10^9
Value contained in nodes will be even number. (Hence when even number of elements in L, median M will be an integer. (even + even) / 2 = integer (aka, not float). So answer will always be integer (never float).)

Sample Test Case:
'''


import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail


# Complete the function below.

# For your reference:
# LinkedListNode {
#    int val
#    LinkedListNode next
# }
def find_median(ptr):
    head = ptr
    l = 0
    while head:
        l += 1
        head = head.next
    is_even = l % 2 == 0
    median = l / 2

    for i in range(median):
        ptr = ptr.next
    out = ptr.val
    if is_even:
        out += ptr.next.val
        out = out / 2
    return out

if __name__ == "__main__":
    f = sys.stdout

    ptr = None
    ptr_tail = None
    ptr_size = int(input())
    ptr_i = 0
    while ptr_i < ptr_size:
        ptr_item = int(input())

        ptr_tail = _insert_node_into_singlylinkedlist(ptr, ptr_tail, ptr_item)
        if ptr_i == 0:
            ptr = ptr_tail
        ptr_i += 1

    # ----added manually----
    ptr_tail.next = ptr
    arbitrary_shift = int(input())
    while (arbitrary_shift > 0):
        arbitrary_shift -= 1
        ptr = ptr.next
    # --------

    res = find_median(ptr)
    f.write(str(res) + "\n")

    f.close()

