from random import randint

#generates list if 10 random numbers
def test():
    a = []
    for i in range(0, 10):
        a.append(randint(0, 10))
    return a

def insertionSort(c):
    n = len(c)
    for i in range(0,n):
        count = i
        while count > 0:
            if c[count] < c[count-1]:
                c[count], c[count-1] = c[count-1], c[count] #moves index to front of list
                count = count - 1
                print(c)
                print()
            else:
              count = 0
        

    return c

b = test()

print("Original: " + str(b))
print()
print("Sorted: " + str(insertionSort(b)))
