class MyException(Exception): pass

def input_positive_number():
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
            
 
def input_number():
    while True:
        try:
            n = int(input())
            return n
        except ValueError:
            print("Value should be int")
            continue
                
def array_init(n:int):
    a = []
    print("Enter elements of array:")
    for q in range(n):
        a.append(input_number())
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
        
def main():
    while True:
        n = input_positive_number()
        array = array_init(n)
        dobutok = count(array)
        print("Result: ", dobutok)

if __name__ == "__main__": 
    main()
        
