# safe function application

# make a function to get x**y in the list
def power_of_pair_in_list(list_of_xy_pairs):
    # create an empty list including the outcome of all the valid pairs
    list_of_outcomes_from_valid_xy_pairs = []
    # loop through the pairs in the list
    for x,y in list_of_xy_pairs:
    # if there is a negative value for y, skip it
        if y < 0:
            continue
    # append valid values of x**y to the empty list
        list_of_outcomes_from_valid_xy_pairs.append(x**y)

    # return the new list
    return list_of_outcomes_from_valid_xy_pairs

pairs = [(5, 2), (3, -1), (4, 3), (2, 0)]
print(power_of_pair_in_list(pairs))