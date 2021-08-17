from Addons import ForTest as Test
from Addons import TestDatas as Datas

def AddTwoNums(l1,l2):

    ResultNode = Datas.ListNode(999) #Dummy
    NextNode = ResultNode
    Carry = 0

    while l1 or l2 or Carry > 0:
        l1_val = 0
        l2_val = 0
        if l1:
            l1_val = l1.val
            l1 = l1.next
        if l2:
            l2_val = l2.val
            l2 = l2.next
        share,left = divmod(l1_val + l2_val + Carry,10)

        Carry = share
        NextNode.next = Datas.ListNode(left)
        NextNode = NextNode.next

    return ResultNode.next


d1 = Test.Create_Custom_LinkedList(2,4,3)
d2 = Test.Create_Custom_LinkedList(5,6,4)
result = AddTwoNums(d1,d2)
Test.Test_Print_ALL_LinkedList(result)