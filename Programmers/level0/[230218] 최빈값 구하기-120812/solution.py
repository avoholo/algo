def solution(array):
    dic = {}
    max_arr = []
    for i in array:
        if i not in dic:
            dic[i] = 1
        elif i in dic:
            dic[i] += 1

    max_val = max(dic.values())
    for k,v in dic.items():
        if v == max_val:
            max_arr.append(k)
    answer = max(max_arr)
    if len(max_arr) > 1:
        return -1
    return answer