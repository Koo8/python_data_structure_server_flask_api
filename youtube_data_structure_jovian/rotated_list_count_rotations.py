'''
You are given "list of numbers", obtained by rotating a "sorted list" an unknown number of times.
Write a function (count_rotations) to determine the "minimum number" of times the original sorted list
was rotated to obtain the given list. Your function should have the worst-case complexity of "O(log N)",
where N is the length of the list. You can assume that all the numbers in the list are "unique".
Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
'''

'''
1.State the problem clearly. Identify the input & output formats. 
    input: a rotated list of numbers
    output: a number to show the time of rotation
2. Come up with some example inputs & outputs. Try to cover all edge case
    [1,2,3,4,5,6,7,8,9,10] -> rotate back to original
    [10,1,2,3,4,5,6,7,8,9] -> rotate once
    [5,6,7,8,9,10,1,2,3,4] -> rotate 6 times
    [2,3,4,5,6,7,8,9,10,1] -> rotate 9 times
    []                     -> empty list  
    [1]                    -> one one element in the list
    [1,2]                  -> two elements in the list 
    
3. Come up with a correct solution for the problem. State it in plain English.
    Sort the (list) to find the smallest number (sortedList[0]), 
    binary_search this smallest number (num) in the list, get the (index)
        register lo, hi and mid
        if mid == num  --> return mid
        if mid > list[0]  --> go to right
        if mid < list[0]  --> go to left 
    return the index -> the end
Implement the solution and test it using example inputs. Fix bugs, if any.
Analyze the algorithm's complexity and identify inefficiencies, if any.
Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
'''

'''
what if the original sorted list has repeated elements [1,2,3,3,3,4,4,5]?
[3,3,4,4,5,1,2,3]
test cases; 
[1,2,3,4,5,6,1,1,] --> the smallest number has duplicates
[1,1]          
[1]
[]
[3,3,3,3,1,2]
[3,3,3,1,2,3]
[3,3,1,2,3,3]
[3,1,2,3,3,3]
[4,5,5,6,6,6,6,6,1,1,2,2,3,3,4,4]
'''
from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases

def binary_search(list, query):
    # register lo, hi and mid
    lo, hi = 0, len(list)-1
    if list[0] == query and list[-1] != query:
        return 0
    while lo <= hi:
        mid = (lo+hi) //2
        print(f'mid is {mid}')
        if list[mid] == query:
            # check if there are duplicates before this mid position
            if list[mid-1] == query:
                hi = mid-1
            else:
                return mid
        elif list[mid] < list[0]:
            print(f'go to left from {mid}')
            hi = mid -1
        elif list[mid] > list[0]:
            print(f'go to right from {mid}')
            lo = mid + 1
        elif mid == 0:
            return 1
        elif list[mid] == list[0] and mid != 0:
            lo = mid +1


    return -1



def count_rotation(list): #target_num): for track a specific num in the rotated list
    #1.sort the list to get the smallest number in the list
    if len(list) ==0:
        return -1
    print(list)
    sorted_list = sorted(list)
    print(f'sorted_list is {sorted_list}')
    start_value = sorted_list[0]
    print(f'start_value is {start_value}')
    rotations = binary_search(list, start_value)
    # if further track a (target_num) in the rotated list
    # result = binary_search(list,target_num)
    return rotations #result+1

tests = [
    {
        'input':{
            'list': [1,2,3,4,5,6,7,8,9,10]
        },
        'output': 0
    },
    {
        'input':{
            'list': [10,1,2,3,4,5,6,7,8,9]
        },
        'output': 1
    },
    {
        'input':{
            'list': [5,6,7,8,9,10,1,2,3,4]
        },
        'output': 6
    },
    {
        'input':{
            'list': [2,3,4,5,6,7,8,9,10,1]
        },
        'output': 9
    },
    {
        'input':{
            'list': []
        },
        'output': -1
    },
    {
        'input':{
            'list': [2,1]
        },
        'output': 1
    },
    {
        'input': {
            'list': [1]
        },
        'output': 0
    },
    {
        'input': {
            'list': [2,3, 1]
        },
        'output': 2
    },
    {
        'input': {
            'list': [3,4,1,2]
        },
        'output': 2
    },


]

result =count_rotation([5,6,7,1,2,3,4], 7)
print(result)
# evaluate_test_cases(count_rotation, tests)

