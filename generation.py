import string
import random
def new_word(length):
    word = ''.join(random.sample(string.digits+string.ascii_letters,length))
    return word


def generate_population(size,min_length,max_length):
    population =[]

    for i in range(size):
        length = i % (max_length-min_length+1)+min_length

        population.append(new_word(length))
    return population

# print(re)