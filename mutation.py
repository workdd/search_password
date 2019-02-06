import random
import string


def word_mutated(word):
    i = int(random.random()*len(word))

    if(i ==0):
        word = random.choice(string.ascii_letters+string.digits)+word[1:]

    else:
        word = word[:i]+random.choice(string.ascii_letters+string.digits)+word[i+1:]
    return word


def population_mutated(population,chance_of_mutation):
    for i in range(len(population)):
        if random.random()*100 <chance_of_mutation:
            population[i]= word_mutated(population[i])
    return population
    