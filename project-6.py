import random;
import time;


def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i;

    return -1;


# my_list = [1, 3, 5, 10, 12];
# print(naive_search(my_list, 10));


def binary_search(list, target, inferior_limit=None, superior_limit=None):
    if inferior_limit is None:
        inferior_limit = 0; #beginning of the list
    if superior_limit is None:
        superior_limit = len(list) -1 #end of the list

    if superior_limit < inferior_limit:
        return -1;

    middle_point = (inferior_limit + superior_limit) // 2;

    if list[middle_point] == target:
        return middle_point;
    elif target < list[middle_point]:
        return binary_search(list, target, inferior_limit, middle_point-1);
    else:
        return binary_search(list, target, middle_point+1, superior_limit);

if __name__=='__main__':
    # my_list = [1, 3, 5, 10, 12];
    # print(binary_search(my_list, 12));

    #Creating a sorted list with 10000 random numbers
    size = 10000;
    initial_set = set();

    while len(initial_set) < size:
        initial_set.add(random.randint(-3 * size, 3 * size));

    sorted_list = sorted(list(initial_set));

    # calculate time with naive_search
    start = time.time();
    for target in sorted_list:
        naive_search(sorted_list, target);

    end = time.time();
    print(f"Time of naive_search: {end - start} seconds ");


    #calculate time with binary_search
    start = time.time();
    for target in sorted_list:
        binary_search(sorted_list, target)
    
    end = time.time();
    print(f"Time of binary_search: {end - start} seconds. ");

