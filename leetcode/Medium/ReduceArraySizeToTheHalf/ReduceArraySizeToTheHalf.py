class Solution:
    def minSetSize(self, arr: 'List[int]') -> int:
        arr_dic = dict()
        for v in arr:
            arr_dic[v] = arr_dic.get(v, 0) + 1
        
        sort_list = sorted(arr_dic.items(), key=lambda x:x[1], reverse=True)
        sumnum = 0
        cnt = 0
        for i in range(0, len(sort_list)):
            sumnum += sort_list[i][1]
            cnt += 1
            if sumnum >= len(arr)//2:
                return cnt
