# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        node1 = l1
        l1_list = []
        while node1 != None:
            l1_list.insert(0, node1.val)
            node1 = node1.next
            
        node2 = l2
        l2_list = []
        while node2 != None:
            l2_list.insert(0, node2.val)
            node2 = node2.next
        
        int_l1 = int("".join([str(s) for s in l1_list]))
        int_l2 = int("".join([str(s) for s in l2_list]))
        add_two_num = int_l1 + int_l2
        
        reverse_list = [int(s) for s in str(add_two_num)][::-1]
        result = ListNode(reverse_list[0])
        for i in reverse_list[1:]:
            result.next = ListNode(i)
            result = result.next
            
        return result
