def sequential_search():
    lst = [1,4,3,7,5,9,8,6,2,10]
    x = 4
    Found=False
    Counter = 0

    for i in range(0,10):
        if x == lst[i]:
            print(lst[i],"found at",i)
            Found=True

    if Found == False:
        print(lst[i],"not found")





def Binary_Search():
    values = (1,12,15,17,190,196,200)
    Target = 17
    MIN = 0
    HIGH = len(values)
    FOUND = False
    ANSWER = 0
    MID = 0

    while (FOUND == False) and (MIN <=HIGH):
        MID = ((MIN + HIGH)//2)
        if values[MID] == Target:
            FOUND = True
            ANSWER = MID
        elif Target > values[MID]:
            MIN = MID + 1
        else:
             HIGH = MID - 1
        print(FOUND, MID)
        if FOUND == True:
            print(Target, "Found as string",ANSWER)
        else:
            print(Target, "was not found")



def bbl_sort():
    lst = [1,4,7,12,5,20]
    for i in range (0, len(lst)):
        for j in range (0,len(lst)-1):
            if lst[j] > lst[j+1]:
                TEMP = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = TEMP
    print(lst)

def selection_sort():
    lst = [1,3,5,7,66,2,3,9,10]
    mini = 0
    x = 0
    TEMP = 0

    for i in range(0,len(lst)-1):
        x = mini
        for j in range(mini+1,len(lst)):
            if lst[j] > lst[mini]:
                x = j
                TEMP = lst[mini]
                lst[mini] = lst[j]
                lst[j] = TEMP
    print(lst)

selection_sort()

def selection_sort():
    lst = [1, 3, 5, 7, 66, 2, 3, 9, 10]

    for i in range(len(lst)-1):
        mini = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[mini]:
                mini = j

        # Swap the found minimum element with the first element
        lst[i], lst[mini] = lst[mini], lst[i]

    print(lst)

selection_sort()




