def isPalindrome(head):
    FastRunner = head
    SlowRunner = head
    Reversed = None

    #Just Move
    while FastRunner and FastRunner.next:
        FastRunner = FastRunner.next.next
        Reversed, Reversed.next, SlowRunner = SlowRunner, Reversed, SlowRunner.next

    #If FastRunner.next is None but FastRunner is not None
    #This occures at LinkedList's size is Odd num.
    if FastRunner:
        SlowRunner = SlowRunner.next

    while Reversed:
        if Reversed.val != SlowRunner.val:
            return False
        Reversed, SlowRunner = Reversed.next, SlowRunner.next

    return True

