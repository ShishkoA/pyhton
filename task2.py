list = [1,2,4,3,53,"rr",456,345,444,254,8,10,9]

def even_numbers(list):
    #input numbers
    even = []
    for item in list:
        if type(item) is int:
            if item == 254:
                break
            elif item % 2 == 0:
                even.append(item)
        else:
            print("It is not number, please type number")

    print(even)

even_numbers(list)