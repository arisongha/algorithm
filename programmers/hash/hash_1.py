
def solution(participant, completion):
    answer = ''
    if len(participant) == 1:
        return participant[0]
    
    compl_dic = dict()
    for c in completion:
        compl_dic[c] = compl_dic.get(c, 0) + 1
    
    part_dic = dict()
    for p in participant:
        part_dic[p] = part_dic.get(p, 0) + 1
        
    for k,v in part_dic.items():
        if compl_dic.get(k) == None:
            return k
        elif compl_dic.get(k) != v:
            return k


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

