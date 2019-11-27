
def solution(n, lost, reserve):
    answer = 0
    reservenlost = set(lost) & set(reserve)
    lost = list(set(lost) - set(reservenlost))
    reserve = list(set(reserve) - set(reservenlost))
    
    bor = []
    for l in lost:
        if l == 1:
            if l+1 in reserve:
                bor.append(l)
                reserve.remove(l+1)
        else:
            if l-1 in reserve:
                bor.append(l)
                reserve.remove(l-1)
            elif l+1 in reserve:
                bor.append(l)
                reserve.remove(l+1)
                
    lost = list(set(lost) - set(bor))
    
    return n-len(lost)


solution(5,[2, 4],[1, 3, 5])

