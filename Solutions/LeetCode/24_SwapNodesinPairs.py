from Addons import ForTest as Test
from Addons import TestDatas as Datas

def SwapNodes(head):

    SwapNode = Datas.ListNode(999) #Dummy
    SwapNode.next = head
    CalNode = SwapNode

    while CalNode.next and CalNode.next.next:
        Buffer = CalNode.next.next.next
        CalNode.next, CalNode.next.next = CalNode.next.next, CalNode.next
        CalNode.next.next.next = Buffer

        CalNode = CalNode.next.next

    return SwapNode.next

Test.Test_Print_ALL_LinkedList(SwapNodes(Test.Create_Custom_LinkedList(1,2,3,4)))