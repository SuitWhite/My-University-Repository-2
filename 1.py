class MyException(Exception): pass

def input_number():
    while True:
        try:
            n = int(input())
            if n<=0:
                raise MyException
            return n
        except MyException:
            print("N<1")
            continue
        except ValueError:
            print("Value should be int")
            continue
                
def array_init(n:int):
    a = []
    print("Enter elements of array:")
    for q in range(n):
        a.append(int(input()))
    return a

def count(array):
    lastplus = array[0]
    for i in range(len(array)):
        if (array[i]>0):
            lastplus = array[i]
    dobutok = 1
    for i in range(len(array)):
        if array[i] == lastplus:
            break
        dobutok *= array[i]
    return dobutok
        

while True:
    n = input_number()
    array = array_init(n)
    dobutok = count(array)
    print("Result: ", dobutok)
        
