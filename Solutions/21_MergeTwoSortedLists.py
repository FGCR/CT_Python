from Solutions.Addons import TestDatas


def MergeLists(first,second):
    merged = TestDatas(999) #Dummy
    merged_next = merged

    while first or second:
        if first and first.val <= second.val:
            merged_next.next = first
            first = first.next
        elif second and first.val > second.val:
            merged_next.next = second
            second = second.next
        merged = merged_next.next

    return merged.next