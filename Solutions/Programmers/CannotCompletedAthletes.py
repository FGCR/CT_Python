import collections


def solution(participant, completion):
    answer = ''

    all_aths = dict(list())
    for c in completion:
        if not (c in all_aths):
            all_aths[c] = list()
        all_aths[c].append(c)
    for p in participant:
        if not p in all_aths:
            return p
        else:
            if all_aths[p]:
                all_aths[p].pop()
            else:
                return p

    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))