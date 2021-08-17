from Addons import ForTest as Test
from Addons import TestDatas as Datas

def ReverseLinkedList(head, left, right):

    if not head or left == right:
        return head

    SuperHead = Datas.ListNode(999) #Dummy
    SuperHead.next = head

    NextNode = SuperHead

    for _ in range(left - 1):
        NextNode = NextNode.next

    EndNode = NextNode.next

    for _ in range(right - left):
        tmp = NextNode.next
        NextNode.next = EndNode.next
        EndNode.next = EndNode.next.next
        NextNode.next.next = tmp

    return SuperHead.next

Test.Test_Print_ALL_LinkedList(ReverseLinkedList(Test.Create_Custom_LinkedList(1,2,3,4,5),2,4))