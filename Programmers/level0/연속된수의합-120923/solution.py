def solution(num, total):
    div = total // num
    start = div - ((num-1) // 2)
    end = div + ((num+2) // 2)
    answer = [i for i in range(start,end)]

    return answer

# 3 12 4 -1 == div - num-1 / 2 
# 5 15 3 -2 == ''
# 4 14 3 -1 == ''
# 5 5  1 -2 == ''