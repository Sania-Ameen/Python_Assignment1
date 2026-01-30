# nested dictionary of strings

# make a function
def new_dictionary_of_strings_length_and_parity(list_of_strings):
    # create an empty dictionary to store the string, length and parity
    dictionary_of_strings_lengths_and_parity = {}
    # loop through the strings in the list and find the length and parity
    for string in list_of_strings:
        length_of_string = len(string)

        if length_of_string % 2 == 0:
            parity_of_string = "even"
        else:
            parity_of_string = "odd"
    # add the length and parity as a new dictionary to each string looped
        dictionary_of_strings_lengths_and_parity[string] = {
        "length": length_of_string,
        "parity": parity_of_string
        }

    return dictionary_of_strings_lengths_and_parity

print(new_dictionary_of_strings_length_and_parity(["hi", "apple", "name"]))