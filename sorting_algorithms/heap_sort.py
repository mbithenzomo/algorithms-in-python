def heapify(my_list, index, heap_size):
    """Converts the list into a max heap.
    """
    # We set the largest number as the root of the heap
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    # We check if the left child of the root exists
    # and is greater than the root
    if left_child < heap_size and my_list[left_child] > my_list[largest]:
        largest = left_child

    # We check if the right child of the root exists
    # and is greater than the root
    if right_child < heap_size and my_list[right_child] > my_list[largest]:
        largest = right_child

    if largest != index:
        # We swap
        my_list[largest], my_list[index] = my_list[index], my_list[largest]
        # Recursion
        heapify(my_list, largest, heap_size)


def heap_sort(my_list):
    """Takes in a list of numbers and performs a heap sort
    Returns the list in ascending order
    """
    # We begin by getting the length of the list
    length = len(my_list)

    # We create a max heap using the heapify function
    for i in range(length, -1, -1):
        heapify(my_list, i, length)

    # We then loop through the list to sort it
    for i in range(length-1, 0, -1):
        # We swap the first and last node
        my_list[0], my_list[i] = my_list[i], my_list[0]
        # We then create a max heap from the reduced list
        heapify(my_list, 0, i)
    return my_list


if __name__ == '__main__':

    my_list = input('Enter a Python list containing numbers:\n')
    print(heap_sort(my_list))
