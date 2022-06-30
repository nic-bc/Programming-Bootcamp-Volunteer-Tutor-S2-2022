def listToInt(my_list: list) -> int:
    """
    Takes in a list and outputs an integer that represents the list.
    E.g. given the list: [8,3,5,1], the output would be 8351.

    Parameters
    ----------
    my_list: list -> the list inputted

    How it works?
    1: the code goes through each element in the list starting from the rightmost element (last element of the list)
    2: it takes the value of that element and multiplies it by its place value.
    3: Then, we store that value in a variable called sum and multiply the place_value variable by 10 because the
       next element will have a place value that's 10 times more than the element on the right
       (e.g. 51 = 50 + 1, 50's place value is ten's which is 10 times more than 1's place value which is one's)
    4: it adds up all of these numbers together to obtain the integer that represents the list

    For example, for the list [3,5,1], we should output 351:
    1: We first start with 1 (the rightmost element in the list) and multiply it with 1 (its place value) -> 1
    2: Secondly, take the 2nd last element 5 and multiply it by 10 (its place value) -> 50
    3: Thirdly, take the 3rd last element 3 and multiply it by 100 (its place value) -> 300
    4: Lastly, we add it up 1 + 50 + 300 = 351
    """

    # initialise sum variable
    # initialise place_value to be 1 for the rightmost element of the list (the one's value)
    sum = 0
    place_value = 1

    # for each element in the list starting from the end of the list (-1) to the 1st element of the list (0-len(my_list)-1)
    # range(start, stop, step). "stop" specifies the position to stop, but that position is not included.
    # Therefore, to reach the 1st element of the list, we need to subtract 1 to include the 1st element of the list.
    for i in range(-1,0-len(my_list)-1,-1):
        # my_list[i] gives us the element, and we multiply each element by its place_value
        # we then add up these numbers to obtain sum, which is the integer that represents the list
        sum = sum + (my_list[i]*place_value)

        # increase the place_value by 10 to move from the one's to the ten's to the hundred's and etc, for the next element
        place_value = place_value*10
    return sum


# test 1 -> output: 8351
print(listToInt([8,3,5,1]))
#test 2 -> output: 0
print(listToInt([0]))
# test 3 -> output: 10000
print(listToInt([1,0,0,0,0]))