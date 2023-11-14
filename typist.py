def typist(s):
    click = 0
    capslock_state = False
    make_list = list(s)
    
    for letter in make_list:
        if letter.islower():
            if capslock_state == False:
                click += 1
            elif capslock_state == True:
                click += 2
                capslock_state = False
        elif letter.isupper():
            if capslock_state == False:
                capslock_state = True
                click += 2
            elif capslock_state == True:
                click += 1
        
    return click