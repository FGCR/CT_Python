def solution(n, computers):
    answer = 0

    roots = [i for i in range(n)]
    for network in computers:
        root = n
        for i in range(len(network)):
            # If Connected
            if network[i] == 1:
                # Root is not Defined
                if root == n:
                    root = i
                else:
                    # All [i] root should be canged to root
                    backup = roots[i]
                    for f in range(len(roots)):
                        if roots[f] == backup:
                            roots[f] = root

    roots.sort()
    bfval = -1
    while roots:
        rootval = roots.pop()
        if bfval != rootval:
            answer += 1
            bfval = rootval

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))