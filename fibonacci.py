def fibonacci(x):
    list = []
    result = ''
    for i in range(0, x):
        if i==0 or i==1:
            list.append(i)
            if i == 0:
                result += "{0}".format(str(i))
            else:
                result += " {0}".format(str(i))
        else:
            add_num = list[i-2] + list[i-1]
            list.append(add_num)
            result += " {0}".format(str(add_num))
    
print(fibonacci(8))
    