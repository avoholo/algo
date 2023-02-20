def solution(quiz):
    answer = []
    for i in quiz:
        equ, ans = i.split(' = ')
        a,oper,b = equ.split()
        if oper == '-':
            answer.append("O") if int(a.replace(" ","")) - int(b.replace(" ","")) == int(ans.replace(" ","")) else answer.append('X')
        else:
            answer.append("O") if int(a.replace(" ","")) + int(b.replace(" ","")) == int(ans.replace(" ","")) else answer.append('X')
    return answer

print(solution(["19 - 6 = 13"]))