import fit
import random
import generation
def compute_performance(population,password):
    performance_list =[]
    
    for individual in population:
        score = fit.fitness(password,individual)
        if score >0:
            predict_length = len(individual)

        performance_list.append([individual,score])

    population_sorted = sorted(performance_list,key = lambda score:score[1],reverse=True)

    return population_sorted, predict_length

def select_survivor(population_sorted,bestsample_count,lucky_sample_count,password_length):
    
    next_generation =[]

    for i in range(bestsample_count):
        if(population_sorted[i][1]>0):
            next_generation.append(population_sorted[i][0])

    lucky_survivored = random.sample(population_sorted,lucky_sample_count)

    for i in range(len(lucky_survivored)):
        next_generation.append(lucky_survivored[i][0])
    
    while len(next_generation) <bestsample_count+lucky_sample_count:
        next_generation.append(generation.new_word(password_length))
    random.shuffle(next_generation)
    return next_generation




