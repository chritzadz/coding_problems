from math import sqrt

def comp(array1, array2):
    state = True
    if array1 == None or array2 == None:
        return False
    else:
        for i in range(len(array2)):
            array2[i] = sqrt(array2[i])
        
        for i in range(len(array2)):
            if array2[i] in array1:
                state = True
            else:
                state = False
                break
        return state

        