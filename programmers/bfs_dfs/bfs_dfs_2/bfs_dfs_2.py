def solution(n, computers):
    li = []
    for i in range(n):
        li.append({i})
    for n1 in range(0, n):
        for n2 in range(n1+1, n):
            if computers[n1][n2] == 1:
                for idx,st in enumerate(li):
                    if n1 in li[idx]:
                        idx1 = idx
                    if n2 in li[idx]:
                        idx2 = idx
                if idx1 != idx2:
                    hap = li[idx1] | li[idx2]
                    li.pop(max(idx2,idx1))
                    li.pop(min(idx1,idx2))
                    li.append(hap)
    
    return len(li)


solution(4, [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]])

