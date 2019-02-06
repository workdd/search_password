def fitness(password,test_word):
    score = 0

    if len(password) != len(test_word):
        return score
    
    get_length_point = 0.5
    score += get_length_point

    get_equal_point =0
    for i in range(len(password)):
        if password[i] == test_word[i]:
            get_equal_point +=1

    score += get_equal_point

    return (score/(len(password)+get_length_point))*100

