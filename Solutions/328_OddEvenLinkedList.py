
#Objective :
# All Odd index Nodes Goes <- Left
# All Even index Nodes Goes -> Right

#Limitations :
#Time Limit : O(n)
#Memory Limit : O(1)

from Addons import ForTest as Test
from Addons import TestDatas as Datas

def OddEvenLinkedList(head):

    if not head:
        return None

    SuperNode = head

    LeftHead = SuperNode
    RightHead = SuperNode.next

    LeftNext = LeftHead
    RightNext = RightHead

    while RightNext and RightNext.next:
        LeftNext.next = LeftNext.next.next
        RightNext.next = RightNext.next.next

        LeftNext = LeftNext.next
        RightNext = RightNext.next

    LeftNext.next = RightHead

    return SuperNode

Test.Test_Print_ALL_LinkedList(OddEvenLinkedList(Test.Create_Custom_LinkedList(1,2,3,4,5,6,7)))