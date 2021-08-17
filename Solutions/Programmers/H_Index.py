def solution(citations):
    answer = 0

    if len(citations) == 1:
        return 1

    sorted_citations = sorted(citations, reverse=True)

    pivot = int(len(sorted_citations) / 2)

    if sorted_citations[pivot] > pivot:
        while pivot < len(sorted_citations) and sorted_citations[pivot] > pivot:
            pivot += 1
        return pivot
    elif sorted_citations[pivot] < pivot:
        while pivot > 0 and sorted_citations[pivot] < pivot:
            pivot -= 1
        return pivot
    else:
        return pivot

    return answer

print(solution([0,0,0,0,0,1,0]))