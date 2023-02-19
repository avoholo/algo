from fractions import Fraction
import math

def solution(a, b):
    myans = Fraction(a / b)
    if myans.denominator > 100000:
        for i in prime(b):
            if i in [2,5]:
                return 1
    if myans.denominator not in [2,5]:
        return 2
    return 1

def prime(n):
    i = 2
    prime_factors = []
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors