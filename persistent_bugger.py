def persistence(n):
    length = len(str(n))
    total = 1
    counter = 0

    while length >= 2:
        make_string = str(n) #'39'
        make_list = list(make_string.strip()) #['3', '9']
        make_list_int = [eval(i) for i in make_list] #[3, 9]

        for number in make_list_int:
            total = total*number
            n = total #n = 27

        total = 1 
        length = len(str(n)) #length masih 2
        counter = counter + 1 #counter = 1

        if length <= 1:
            break

    return counter

result = persistence(333333)
print(result)