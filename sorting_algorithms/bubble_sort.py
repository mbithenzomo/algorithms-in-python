def bubble_sort(my_list):
    """Takes in a list of numbers and performs a bubble sort
    Returns the list in ascending order
    """
    # We begin by getting the length of the list
    length = len(my_list)

    # We then loop through the list to sort it
    for number in range(length):
        swapped = False
        # Use length-1 to avoid an index out of range error
        for index in range(length-1):
            # This next part is where the swap happens.
            # Basically, we are checking whether the number in question
            # is greater than the number to its right.
            # If it is, then they are swapped.
            if my_list[index] > my_list[index+1]:
                swapped = True
                my_list[index], my_list[index+1] = my_list[index+1], \
                    my_list[index]
        if not swapped:
            break  # Stop iteration if the list is sorted
    return my_list


if __name__ == '__main__':

    my_list = input('Enter a Python list containing numbers:\n')
    print(bubble_sort(my_list))
