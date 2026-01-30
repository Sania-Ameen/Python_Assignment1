# distribution analysis

# define the function
def list_to_dictionary(list_of_numbers):
    # create an empty dictionary to store unique keys and values from the list
    dictionary_of_unique_keys_and_values = {}

    # find the total numbers in the list to calculate the percentage
    total_values_in_list = len(list_of_numbers)

    # loop through the list
    for value in list_of_numbers:
    # if the key is not in the dictionary already
        if value not in dictionary_of_unique_keys_and_values:
        # counter for elements in the list that are less than or equal to that key
            element_less_than_or_equal_to_key_counter = 0

        # loop through the numbers in the list again and count if the number is <= value
            for number in list_of_numbers:
                if number <= value:
                    element_less_than_or_equal_to_key_counter = element_less_than_or_equal_to_key_counter + 1

        # compute the percentage of the elements that are less than or equal to the key

            percentage_of_elements_less_than_or_equal_to_key = (element_less_than_or_equal_to_key_counter/ total_values_in_list) * 100

        # set the values in the dictionary as the percentage outcome
            dictionary_of_unique_keys_and_values[value] = percentage_of_elements_less_than_or_equal_to_key

    # sort the dictionary by key

    sorted_dictionary = dict(sorted(dictionary_of_unique_keys_and_values.items()))

    # return the sorted dictionary

    return sorted_dictionary


print(list_to_dictionary([3, 1, 2, 3, 4, 2]))
