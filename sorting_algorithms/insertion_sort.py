def insertion_sort(my_list):
    """Takes in a list of numbers and performs an insertion sort
    Returns the list in ascending order
    """
    # Loop through the list
    for i in range(1, len(my_list)):
        while 0 < i and my_list[i] < my_list[i - 1]:
            # For each number in the list that is greater
            # than the current number, swap
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
            # Decrease the counter
            i -= 1

    return my_list


if __name__ == '__main__':

    my_list = input('Enter a Python list containing numbers:\n')
    print(insertion_sort(my_list))
