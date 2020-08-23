import random
import time

def random_numbers_generator():
    l = []
    for i in range(999):
        l.append(random.randint(0,999))
    return l

unsorted_l = random_numbers_generator()

#print(unsorted_l)

start = time.time()

def insertion_sort(unsorted_list):
    sorted_list = []
    while(len(unsorted_list) > 0):
        smallest_element = unsorted_list[0] # just for the start we define that the smallest element is on position 0 in list
        smallest_index = 0
        for index, element in enumerate(unsorted_list): # getting the index besides the values of the elements
            if element < smallest_element:
                smallest_element = element
                smallest_index = index
        unsorted_list.pop(smallest_index) # removing the element in the original list by index
        sorted_list.append(smallest_element)

    return sorted_list

print(insertion_sort(unsorted_l))

end = time.time()
print(end - start) # checks the amount of time the algorithm needs to sort the list