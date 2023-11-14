def two_are_positive(a, b, c):
    counter = 0
    list = [a,b,c]
    for number in list:
        if number > 0:
            counter = counter + 1
        if number <= 0:
            counter = counter
    if counter == 2:
        return True
    else:
        return False
    