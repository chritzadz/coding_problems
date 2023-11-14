def solver(upper_bound):
    for i in range(upper_bound):
        if (i+100)**0.5 == (int(1+100))**0.5 and (i+268)**0.5 == (int(1+268))**0.5:
            print(i)

solver(1000)
