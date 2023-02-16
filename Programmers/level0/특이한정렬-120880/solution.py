def solution(numlist, n):
    answer = []
    dic = {i : abs(i-n) for i in numlist}
    li = list(dict(sorted(dic.items(), key=lambda item: item[1])).items())
    
    answer.append(li[0][0])
    for i in range(1,len(li)):
        answer.append(li[i][0])
        if(li[i-1][1] == li[i][1] and li[i][0] > li[i-1][0]):
            tmp = answer[i-1]
            answer[i-1] = answer[i]
            answer[i] = tmp
    return answer