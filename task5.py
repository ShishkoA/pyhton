#Develop a function that takes a list of integers (by idea not in fact) as an argument and returns list of top-three max integers.
#If passed list contains not just integers collect them and print the following error message: You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. 
#If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but some list should be returned in any case.
# elements in an array
import sys
 
# Function to print three largest
# elements
def print3largest(arr, arr_size):
 
    # There should be atleast three
    # elements
    if (arr_size < 3):
     
        print(" Invalid Input ")
        return

    for x in arr:
        if int(x) == x:
    	    pass
        else:
            print("I can't parse:")

    third = first = second = -sys.maxsize
     
    for i in range(0, arr_size):
     
        # If current element is greater
        # than first
        if (arr[i] > first):
         
            third = second
            second = first
            first = arr[i]
         
 
        # If arr[i] is in between first
        # and second then update second
        elif (arr[i] > second):
         
            third = second
            second = arr[i]
         
        elif (arr[i] > third):
            third = arr[i]
     
    print("Three largest elements are",
                  first, second, third)
 
# Driver program to test above function
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)