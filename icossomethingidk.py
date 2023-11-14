def sequence(x):
    return [13*i**2 - 12*i for i in range(x+1)]

def icos(x):
    list = sequence(x)
    return(True if x in list else False)