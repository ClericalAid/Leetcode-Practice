# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    """
    Perform a recursion down the linked list

    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addLink(l1, l2, 0)
    
    """
    Adding two numbers together represented as a linked list

    Cases:
    1)
    The numbers overflow above 10:
        Add one to the next number
    2)
    One number is nullptr:
        Take the number that is not nullptr (check for overflow)
    3)
    Both numbers are nullptr:
        Leave it blank, or it can become a 1 if there is overflow

    The recursion adds the two numbers at the current node, then goes down the chain
    carrying over any overflow
    """
    def addLink(self, l1, l2, carryOver):
        if l1 == None and l2 == None and carryOver == 0:
            return None

        if l1 == None:
            l1 = ListNode(0)

        if l2 == None:
            l2 = ListNode(0)

        ret = ListNode(0)
        ret.val = l1.val + l2.val + carryOver
        if ret.val >= 10:
            ret.val -= 10
            carryOver = 1
        else:
            carryOver = 0

        ret.next = self.addLink(l1.next, l2.next, carryOver)
        return ret

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val)
  result = result.next
