from markposition import mark_as_counted, check_if_counted, reset_all_to_not_counted

def get_feedback(code, guess):
    black_key_pegs_count = white_key_pegs_count = 0
    reset_all_to_not_counted()

    code_list = list(code)
    guess_list = list(guess)

    for i in range(0, len(code_list)):
        if code_list[i] == guess_list[i]:
            black_key_pegs_count += 1
            code_list[i] = None
            guess_list[i] = None
            mark_as_counted(i)
            
    for i in range(0, len(guess_list)):
        for j in range(0, len(code_list)):
            if code_list[j] == guess_list[i] and check_if_counted(j) == False:
                if code_list[j] == None or guess_list[i] == None:
                    pass
                else:
                    white_key_pegs_count += 1
                    mark_as_counted(j)
                    break
            
    key = 'b' * black_key_pegs_count + 'w' * white_key_pegs_count
    return key
                

print(get_feedback("RRPBOO", "RPOBOO"))