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
        if crossing_points[idx] is None:
            childs.append([parents[0], parents[1]])

            parent_1_bits = '{:08b}'.format(parents[0])
            parent_2_bits = '{:08b}'.format(parents[1])

            print('Parent {} A ({}): '.format(idx, parents[0]), parent_1_bits)
            print('Parent {} B ({}): '.format(idx, parents[1]), parent_2_bits)
            print('Child A: ', child_1)
            print('Child B: ', child_2)
            print('\n')
        else:
            parent_1_bits = '{:08b}'.format(parents[0])
            parent_2_bits = '{:08b}'.format(parents[1])

            child_1 = parent_1_bits[0: crossing_points[idx][0]] + parent_2_bits[crossing_points[idx]
                                                                                [0]: crossing_points[idx][1]+1]+parent_1_bits[crossing_points[idx][1]+1:]

            child_2 = parent_2_bits[0: crossing_points[idx][0]] + parent_1_bits[crossing_points[idx]
                                                                                [0]: crossing_points[idx][1]+1]+parent_2_bits[crossing_points[idx][1]+1:]
            print('Parent {} A ({}): '.format(idx, parents[0]), parent_1_bits)
            print('Parent {} B ({}): '.format(idx, parents[1]), parent_2_bits)
            print('Crossing points: ', crossing_points[idx])
            print('Child A ({}): '.format(int(child_1, 2)), child_1)
            print('Child B ({}): '.format(int(child_2, 2)), child_2)
            print('\n')


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

cross(selected_parents, crossing_points)
