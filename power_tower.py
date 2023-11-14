def power_tower(n, x):
    power = x
    for i in range(n-1):
        result = x**power
        power = result
    
    return power

print(power_tower(4, 2))

def power_tower_cc(n, x):
    if n == 1:
        return x
    else:
        return x**power_tower(n-1, x)
    
print(power_tower(4, 2))