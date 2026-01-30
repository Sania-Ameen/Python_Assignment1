# controlled multiplication

threshold_value = 100
product = 1
current_number = 1

# while the product is <= threshold_value multiply consecutive integers starting from "current_number"

while product <= threshold_value:
    product = product * current_number
    current_number = current_number + 1
# out of the while loop, print the product and the current_number - 1 (because of the new pointer in the loop)
print(product)
print(current_number - 1)


