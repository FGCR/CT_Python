from Addons import ForTest as Test
from Addons import TestDatas as ListNode

def ReverseLinkedList(head : ListNode):
    Reversed = None
    NextNode = head;

    while NextNode:
        Reversed, Reversed.next, NextNode = NextNode, Reversed, NextNode.next

    return Reversed

result = ReverseLinkedList(Test.Create_Default_LinkedList())
Test.Test_Print_ALL_LinkedList(result)