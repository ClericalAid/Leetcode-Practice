# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    2 ways to solve it:

    Stack
        Push all the nodes onto a stack
        Pop them off and assemble the list as we pop them
        Set our last node's "next" member variable to None
        GG baby easy money

    Recursion
        Check the recurse function
    """
    def reverseList(self, head: ListNode) -> ListNode:
        stackMethod = False
        if head == None:
            return None
        if stackMethod == True:
            stack = []
            currNode = head
            while currNode != None:
                stack.append(currNode)
                currNode = currNode.next

            currNode = stack.pop()
            newHead = currNode
            while len(stack) > 0:
                currNode.next = stack.pop()
                currNode = currNode.next
            currNode.next = None
            return newHead

        else:
            return self.recurse(head, None)

    """
    recurse
    parameters:
        currNode
            The node which we are currently working on
        prevNode
            The node which came before the current node

    A recurion where we go to the end of the list, then build it back recursively. Save the next
    node in a temp variable. Set the current node's next node as the previous node (the 
    reversing).

    Then we have our 2 cases:
    We are not at the last node
        Continue down the chain

    We are at the last node
        Return this node (it's the new head)
    """
    def recurse(self, currNode, prevNode):
        nextNode = currNode.next
        currNode.next = prevNode

        if nextNode != None:
            return self.recurse(nextNode, currNode)
        else:
            return currNode

def printList(headNode):
    currNode = headNode
    while currNode != None:
        print(currNode.val)
        currNode = currNode.next

testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

printList(testHead)
solver = Solution()
reversedHead = solver.reverseList(testHead)
printList(reversedHead)
