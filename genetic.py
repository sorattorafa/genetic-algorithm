import math
import itertools
import random
import numpy


def function(x):
    return math.sin((math.pi * x) / 256)


def compute_fitness(population):
    f_x = list(map(function, population))
    f_sum = sum(f_x)
    f_norm = list(map(lambda x: x/f_sum, f_x))
    f_acm = list(itertools.accumulate(f_norm))
    return f_acm


def selection(population, f_acm, random_numbers):
    # random_numbers = [random.random()] * len(f_acm)

    selected_parents_idx = []
    for number in random_numbers:
        idx = 0
        while idx < len(f_acm) and f_acm[idx] < number:
            idx += 1
        selected_parents_idx.append(idx + 1)

    selected_parents = [population[idx-1] for idx in selected_parents_idx]
    selected_parents = list(numpy.reshape(selected_parents, (-1, 2)))

    print('Selected parents indexes: ', selected_parents_idx)
    print('Selected parents: ', selected_parents)
    print('\n')

    return selected_parents


def cross(selected_parents, crossing_points):
    childs = []
    for idx, parents in enumerate(selected_parents):
        parents = ('{:08b}'.format(parents[0]), '{:08b}'.format(parents[1]))

        if crossing_points[idx] is None:
            childs.extend(parents)
        else:
            start = crossing_points[idx][0]
            end = crossing_points[idx][1]

            child1 = parents[0][:start] + \
                parents[1][start:end+1] + parents[0][end+1:]

            child2 = parents[1][:start] + \
                parents[0][start:end+1] + parents[1][end+1:]

            childs.extend([child1, child2])

    return childs


def mutate(individuals, idx):

    def swap_bit(str, pos):
        new_bit = '0' if str[pos] == '1' else '0'
        return str[:pos] + new_bit + str[pos+1:]

    idx -= 1

    individual_idx = int(idx / 8)
    individual_offset = idx % 8

    individuals[individual_idx] = swap_bit(
        individuals[individual_idx], individual_offset)

    print('individual_idx', individual_idx)
    print('individual_offset', individual_offset)


population = [189, 216, 99, 236, 174, 75, 35, 53]


f_acm = compute_fitness(population)
selected_parents = selection(population, f_acm, [0.293, 0.971,
                                                 0.160, 0.169, 0.664, 0.568, 0.371, 0.109])

crossing_points = [
    (3, 5),
    (1, 3),
    (2, 6),
    None


]

childs = cross(selected_parents, crossing_points)
print('childs', childs)
mutate(childs, 17)
print('mutated childs', childs)
