def is_prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


def num_prime(lower_bound, upper_bound):
    counter = 0
    for i in range(lower_bound, upper_bound+1):
        if i >= 2:
            if is_prime(i):
                counter += 1
        else:
            pass
    return counter

print(num_prime(0,10))
