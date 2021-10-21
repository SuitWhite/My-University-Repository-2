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
        
def modul(a):
    if (a>=0):
        return a
    else:
        return -1*a
        
def matrix_init(N:int):
    a = []
    for i in range(N):
        a.append([0]*N)
    for i in range(N):
        for j in range(N):
            a[i][j] = (i-j)
    return a
    
def show_matrix(matrix, size_of_matrix):
    for i in range(size_of_matrix):
        ryadok = ""
        for j in range(size_of_matrix):
            ryadok+=str(modul(matrix[i][j])+1)
            ryadok+=" "
        print(ryadok)
        
def Exit():
    print("Вийти з програми? (y,n):")
    ch = input()
    if (ch=='y'):
        exit()
 
def main():       
    while True:
        N = input_positive_number()
        A = matrix_init(N)
        show_matrix(A,N)
        Exit()
        
if __name__ == "__main__": 
    main()
