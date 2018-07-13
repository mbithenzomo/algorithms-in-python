def quick_sort(my_list):
    """Takes in a list of numbers and performs a quick sort
    Returns the list in ascending order
    """
    length = len(my_list)

    # If list contains only 1 number or no numbers at all
    if(length <= 1):
        return my_list

    else:
        # Set the pivot to be the first number in the list
        pivot = my_list[0]
        # Get list of all numbers greater than the pivot
        greater = [number for number in my_list[1:] if number > pivot]
        # Get list of all numbers lesser than or equal to the pivot
        lesser = [number for number in my_list[1:] if number <= pivot]
        # Recursively get sorted list
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':

    my_list = input('Enter a Python list containing numbers:\n')
    print(quick_sort(my_list))
