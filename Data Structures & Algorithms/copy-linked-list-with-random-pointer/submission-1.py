"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # strategy: old to new table
    # iterate through the linked list
    # store prev
    # create a new node with the value of curr
    # table[prev].next = new node
    # prev = curr
    # curr = curr.next

    # now that the main list is created, 
    # for each node in orig
    # update that new copy's random to the new node copy of the old node's random
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # initialize the head
        table = {}
        if head is None:
            return None

        new_head = Node(head.val)
        table[head] = new_head

        prev = head 
        curr = head.next
        while curr:
            # create a new node 
            new_n = Node(curr.val)
            table[curr] = new_n

            table[prev].next = new_n

            prev = curr
            curr = curr.next


        # iterate again, updating random pointers
        # cannot do this inline as we need the copy in the future
        prev = None
        curr = head
        while curr:
            if curr.random is not None:
                table[curr].random = table[curr.random]


            prev = curr
            curr = curr.next



        return table[head]



        