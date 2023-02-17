def quick_sort(str):
    if len(str) <= 1:
        return str
    pivot = str[len(str) // 2]
    les_piv, eql_piv, gtr_piv = [], [], []
    for i in range(len(str)):
        if str[i] < pivot:
            les_piv.append(str[i])
        elif str[i] > pivot:
            gtr_piv.append(str[i])
        else:
            eql_piv.append(str[i])
    return quick_sort(les_piv) + eql_piv + quick_sort(gtr_piv)

def solution(my_string):
    answer = quick_sort(my_string.lower())
    return ''.join(answer)