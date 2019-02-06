import generation
import fit
import create_children
import mutation
import compute_and_select
import random
import string

password =input('패스워드를 입력하세요:\n')

generation_count = 1000000
population =100
bestsample_count = 20
lucky_sample = 20
child_count =5
chance_of_mutation = 10
min_length =2
max_length =10
pop = generation.generate_population(size = population,min_length=min_length,max_length=max_length)

for g in range(generation_count):
    pop_sorted,pred_length = compute_and_select.compute_performance(population=pop,password=password)

    if int(pop_sorted[0][1])== 100:
        print('Success! The password is %s' % (pop_sorted[0][0]))
        break
    survivors = compute_and_select.select_survivor(pop_sorted,bestsample_count,lucky_sample,pred_length)

    children =create_children.create_children(parents=survivors,child_count=child_count)

    new_generation =mutation.population_mutated(population=children,chance_of_mutation=chance_of_mutation)

    pop = new_generation

    print("----%s번째 세대입니다."%(g+1))
    print(pop_sorted[0])
