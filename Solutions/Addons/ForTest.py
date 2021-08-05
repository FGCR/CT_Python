from . import TestDatas

def Create_Default_LinkedList() -> TestDatas:
    l5 = TestDatas.ListNode(5)
    l4 = TestDatas.ListNode(4, l5)
    l3 = TestDatas.ListNode(3, l4)
    l2 = TestDatas.ListNode(2, l3)
    l1 = TestDatas.ListNode(1, l2)

    return l1

def Create_Custom_LinkedList(*args) -> TestDatas:

    StartNode = TestDatas.ListNode(args[0])
    CurrentNode = StartNode

    for i in range(len(args) - 1):

        CurrentNode.next = TestDatas.ListNode(args[i + 1])
        CurrentNode = CurrentNode.next

    return StartNode

def Test_Print_ALL_LinkedList(head : TestDatas):
    print("----RESULT----")
    i = 0
    while head:
        print(i," : ",head.val)
        i += 1
        head = head.next