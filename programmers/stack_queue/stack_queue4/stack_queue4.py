def solution(bridge_length, weight, truck_weights):
    sec = 0
    que = []
    temp_que = []
    truck_weights_copy = truck_weights.copy()
    while len(que) != len(truck_weights) :
        sec += 1
        flag = False
        if len(truck_weights_copy) != 0 and sum(temp_que) + truck_weights_copy[0] <= weight:
            temp_que.append(truck_weights_copy.pop(0))
            
        if sec != 0 and sec > bridge_length:
            que.append(temp_que.pop(0))
        
    return sec
