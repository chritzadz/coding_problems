def base7(price):
    list = []
    while price > 0:
        list.append(price%7)
        price = price // 7
    return list

def kurang(price):
    base_list = base7(price)
    list = base7(price)
    for i in range(len(list)):
        list[i] = base_list[i]-1 if base_list[i] != 0 else 0
       
    kurang = 0   
    for i in range(len(base_list)):
        kurang += 7**i*list[i]
    return kurang

def kembalian(price):
    base_list = base7(price)
    index_list_zero = []
    for i in range(len(base_list)):
        if base_list[i] == 0:
            index_list_zero.append(i)
        else: 
            continue
    
    add_value = 0
    for i in index_list_zero:
        add_value += 7**i
        
    kembalian = add_value - kurang(price)
    return kembalian

def bisa_transaksi(price):
    state = True
    final_list = base7(kembalian(price))
    for i in final_list:
        if i == 0 or i == 1:
            state = True
        if i > 1:
            state = False
            break
    return state
    
    
    
print(bisa_transaksi(2442)) 