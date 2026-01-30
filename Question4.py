# sorted search with conditions

from random import random

list_of_random_values_between_zero_and_one = [random() for i in range(20)]
random_x_value = random()

# sort the randomized list
list_of_random_values_between_zero_and_one.sort()

# create a counter for the index in the list
index_of_list = 0
# loop through each value of the list
for value_of_index in list_of_random_values_between_zero_and_one:
    # conditional if the value of the index is greater than or equal to the randomized x value
    if value_of_index >= random_x_value:
        # print statements
        print("Sorted list:", list_of_random_values_between_zero_and_one)
        print("x:", random_x_value)
        print("First matching index:", index_of_list)
        # break the loop once a value greater than x is found
        break
    # if the if conditional is not met move to the next index (+1)
    index_of_list = index_of_list + 1




