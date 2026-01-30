# circle area comparison with validation

# import the math library
import math
# make the function
def circle_area_coverage(radius_of_circle1,radius_of_circle2):

    # only evaluate for positive integers
    # if the radii are not integers print an error message
    if radius_of_circle1 % 1 != 0 or radius_of_circle2 % 1 != 0:
        return "ERROR: YOU MUST ENTER AN INTEGER FOR BOTH RADII"
    # if the radii are negative print an error message
    elif radius_of_circle1 <= 0 or radius_of_circle2 <= 0:
        return "ERROR: YOU MUST ENTER A POSITIVE VALUE FOR BOTH RADII"

    # calculate the area for each circle
    area_of_circle1 = math.pi * radius_of_circle1**2
    area_of_circle2 = math.pi * radius_of_circle2**2

    # find the larger area out of the two circles
    larger_area_of_circle = max(area_of_circle1,area_of_circle2)
    smaller_area_of_circle = min(area_of_circle1,area_of_circle2)

    # calculate the remaining area of the larger circle with respect to the smaller circle
    percentage_of_coverage = (smaller_area_of_circle / larger_area_of_circle) * 100

    # return the percentage
    return percentage_of_coverage

print(circle_area_coverage(3,5))
