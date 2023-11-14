def PrimeOrNot(x):
    state = True
    for i in range(2, x):
        if x%i == 0:
            state = False
            break
    return state

def PrimeFactorsSum(pfs):
    list = []
    result = 0
    for i in range(2, pfs):
        if PrimeOrNot(i) == True:
            list.append(i) 
        else:
            pass 
        
    kpk = []  
    while not PrimeOrNot(int(pfs)):
        for i in list:
            if int(pfs/i) == pfs/i:
                kpk.append(i)
                pfs = pfs/i 
                if PrimeOrNot(int(pfs)):
                    kpk.append(int(pfs))
                    break
                else:
                    break
    for i in kpk:
        result += i  
    return pfs if result == 0 else result

def DivisorSum(ds):
    result = 0
    for i in range(1, ds+1):
        if ds%i == 0:
            result += i
        else:
            pass
    return result
        
def ds_multof_pfs(nMin, nMax):
    result = []
    for i in range(nMin, nMax):
        if DivisorSum(i)%PrimeFactorsSum(i) == 0:
            result.append(i)
        else:
            pass
    return result
        
print(ds_multof_pfs(10, 110))
