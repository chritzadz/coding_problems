def get_feedback(code, guess):
    feedback = ''
    code = list(code)
    guess = list(guess)))

    for i in range(0, len(code)):
        if code[i] == guess[i]:
            feedback += "b"
            del code[i]
            del guess[i]
        else:
            continue

    for i in range(0, len(guess)):
        for j in range(0, len(code)):
                if guess[i] == code[j] and i != j:
                    feedback += "w"
                    del code[j]
                    del guess[i]
                    break
    return feedback
                