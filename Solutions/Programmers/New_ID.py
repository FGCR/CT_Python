import re
def solution(new_id):
    answer = ''

    answer = re.sub('[^-_.a-z0-9]', '', new_id.lower())
    while ".." in answer:
        answer = answer.replace("..", ".")
    while len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    while len(answer) > 0 and answer[len(answer) - 1] == '.':
        answer = answer[0:len(answer) - 1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) > 15:
        answer = answer[0:15]
    while answer[len(answer) - 1] == '.':
        answer = answer[0:len(answer) - 1]
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("......................."))