from math import gcd

def is_relative_prime(a, b):
    return gcd(a, b) == 1

print(is_relative_prime(4, 2))