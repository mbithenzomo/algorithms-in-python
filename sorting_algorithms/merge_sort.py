def merge_sort(my_list):
    """Takes in a list of numbers and performs a merge sort
    Returns the list in ascending order
    """
    length = len(my_list)
    if length > 1:
        # Divide list into roughly 2 halves
        midpoint = length // 2
        # Recursively sort first half
        left_half = merge_sort(my_list[:midpoint])
        # Recursively sort second half
        right_half = merge_sort(my_list[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            my_list[k] = right_half[j]
            j += 1
            k += 1

    return my_list


if __name__ == '__main__':

    my_list = input('Enter a Python list containing numbers:\n')
    print(merge_sort(my_list))
