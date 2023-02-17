def solution(babbling):
    babble_sets = ["aya", "ye", "woo", "ma"]
    answer = 0
    for x in babbling:
        for y in babble_sets:
            if y in x:
                x = x.replace(y,' ')
        if x.islower() == False:
            answer += 1
    return answer