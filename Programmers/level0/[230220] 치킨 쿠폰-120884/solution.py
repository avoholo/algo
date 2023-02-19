def solution(chicken):
    coupons = 0
    answer = 0
    while chicken > 0:
        chicken -= 1
        coupons += 1
        if coupons == 10:
            coupons = 0
            chicken += 1
            answer += 1
    return answer