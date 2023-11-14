def dashatize(n):
    
    make_string = str(n)
    make_list = list(make_string.strip())
    test = []
    result = []
    
    for y in make_list:
        if not y.isdigit():
            None
        else: 
            None
            
    make_list_int = [int(i) for i in make_list]
    make_list_int.append(1)

    for number in make_list_int:
        positions_odd = []
        for a in range(len(test)):
            if test[a] == "odd":
                positions_odd.append(a)

        if (number % 2) == 0: 
            test.append("even")
            position = make_list_int.index(number)
            kesel = make_list_int[position] + make_list_int[position+1]
            if (kesel % 2) > 0:
                result.append(str(number) + "-")
            if (kesel % 2) == 0:
                result.append(str(number))
        if (number % 2) >= 1:
            test.append("odd")
            position = make_list_int.index(number)
            result.append(str(number) + "-")

    final_result_1 = ''.join(result)
    final_result_2 = final_result_1[:-3]

    return final_result_2


print(dashatize(545))