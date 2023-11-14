def increment_string(strng):
    check_digit = any(char.isdigit() for char in strng)
    make_list = []
    digit_list = []
    huruf_list = []
    tof = []
    
    if check_digit == False:
        final = strng + "1"
        
    if check_digit == True:
        make_list = list(strng)
        make_list.reverse()
        for num in make_list:
            if num.isdigit():
                digit_list.append(num)
            if not num.isdigit():
                position = make_list.index(num)
                from_behind = position - len(make_list)
                huruf_list = make_list[from_behind:]
                break
                
        digit_list.reverse()
        huruf_list.reverse()
        
        number_plus_one = int(''.join(digit_list))
        tambahin = number_plus_one + 1
        number_9 = '9'
        
        for number in digit_list:
            if number_9 != number:
                result = False
                break
            else:
                result = True
        
        return digit_list, result
        
        if result == True:
            digit_list.clear()
            digit_list.append(tambahin)
            final = ''.join(digit_list)
        if result == False:
            ''.join(digit_list)
            
            .replace("bananas", "apples")
#        if result == False: