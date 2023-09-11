"""
Example 1: Search in a sorted array
"""

import random

def generate_sequence(length = 16):
    """
    Generate a sequence of sorted numbers
    :param length: the length of the array
    :return:
    """

    my_list = []   # initialize an empty list
    initial = random.randint(10, 50)  # create the first element at random
    my_list.append(initial)  # put the first element in the list
    for i in range(length - 1):
        increment = random.randint(10, 20)   # create the distance to increase the element
        my_list.append(my_list[-1] + increment)  # put the new number in the list

    return my_list

    # return sorted([random.randint(10, 300) for _ in range(length)])

def do_search(my_list, number):
    """
    Search for `number` in `my_list`
    :param my_list: the list of number (sorted!)
    :param number: the number to search for
    :return: The index of the number
    """
    my_index = 0   # initially the pointer is at the first position
    is_found = False # flag --> if the number was founder, set this to true
    while not is_found:
        if my_list[my_index] < number:
            # the number pointer points to is smaller than the target number
            # the number is at the right
            # move the pointer to the right
            my_index += 1
        elif my_list[my_index] == number:
            # if the number the pointer points to is the target
            # found!
            # set found to be true
            is_found = True
            break

    return my_index




if __name__ == "__main__":
    my_list = generate_sequence()  # generate sequence of number
    print("My list is now: ", my_list)
    to_search = int(input("Enter the number to search: "))
    my_index = do_search(my_list, to_search)  # do search
    print("Found! Index is %d! " % my_index)

