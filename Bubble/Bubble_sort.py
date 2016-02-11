import random
import time
samples = []

def generate_list(number_of_elements):
    list = [x + 1 for x in range(50000)]
    random.shuffle(list)
    return list

def remove_max(samples):
    samples.remove(max(samples))

def remove_min(samples):
   samples.remove(min(samples))

def calculate_average(number_of_elements):
    average = sum(samples)/len(samples)
    return average

def buildin_sort(list):
    return list.sort()

def bubble_sort(list):
    for i in range(len(list), 0, -1):
        for j in range(0, len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

def time_taken_by_sort(number_of_elements, way_of_sorting):

    random_list = generate_list(number_of_elements)

    number_of_checks = 3
    for i in range (number_of_checks):
        start = time.time()
        way_of_sorting (list(random_list))
        finish = time.time()
        samples.append(finish - start)

    remove_max(samples)
    remove_min(samples)
    average_time = calculate_average(samples)

    print('Time taken by sorting of ' +  str(number_of_elements) +  ' is ' + str(average_time))
    print average_time

time_taken_by_sort(50000,bubble_sort)
time_taken_by_sort(50000,buildin_sort )