
def solution(priorities, location):
    seq = list(range(0,len(priorities)))
    i = 0
    count = 0
    while True:
        before_priorities = priorities.copy()
        if i == len(priorities)-1:
            i=0
        if priorities[i] < max(priorities[i+1:]):
            priorities.append(priorities.pop(i))
            seq.append(seq.pop(i))
        
        i+=1
        
        if before_priorities == priorities:
            count += 1
        else:
            count = 0
            
        if count == len(priorities)-1:
            break
            
    return seq.index(location)+1



solution([2, 2, 9, 1, 3, 4], 3)

