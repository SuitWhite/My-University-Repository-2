def modul(a):
    if (a>=0):
        return a
    else:
        return -1*a
        
class MyException(Exception): pass
while True:
    try:
        N = input()
        if (N=="exit"):
            break
        N = int(N)
        if (N<1):
            raise MyException
        A = []
        for i in range(N):
            A.append([0]*N)
        for i in range(N):
            for j in range(N):
                A[i][j] = (i-j)
        for i in range(N):
            ryadok = ""
            for j in range(N):
                ryadok+=str(modul(A[i][j])+1)
                ryadok+=" "
            print(ryadok)
        print("If you want to exit, enter ""exit"" ")
    except MyException:
        print("N<1")
        continue
    except ValueError:
        print("Value should be int")
        continue