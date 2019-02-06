import random
def create_child(i1,i2):
    child =''

    child_min_length = min(len(i1),len(i2))

    for i in range(child_min_length):
        if(int(random.random()*100)<50):
            child += i1[i]
        else:
            child +=i2[i]
    return child


def create_children(parents,child_count):
    next_population =[]
    for i in range(int(len(parents)/2)):
        for j in range(child_count):
            next_population.append(create_child(parents[i],parents[len(parents)-1-j]))
    return next_population

