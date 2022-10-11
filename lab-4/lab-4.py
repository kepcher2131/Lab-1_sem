"""                                                 9. Формируется матрица F следующим образом: если в В количество строк, состоящих из одних нулей в четных столбцах в области 2 больше, 
E | B   Вид матрицы       2     Вид подматрицы      чем сумма положительных  элементов в четных строках в области 4,
D | C                   1   3                       то поменять в С симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. 
                          4                         После чего вычисляется выражение: ((К*F)*А)–(K*A^T). Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import random
import time
import os

def print_matrix(M):
    for i in M:
        for j in i:
            print("%3d" % j, end = ' ')
        print()
    print()

def submatrix(M):
    for i in range(size):
        M.append([0]*size)

try:
    
    row_q = int(input("Введите чётное количество строк (столбцов) квадратной матрицы >5:"))
    while row_q <6 or row_q%2 !=0:
        row_q = int(input("Введите чётное!!! количество строк (столбцов) квадратной матрицы >5!!!:"))
    K = int(input("Введите число К="))
    
    start = time.time()
    print("\n-----Результат работы программы-----\n -----Локальное время",time.ctime(),"-----")

    A, F, AF, AT = [], [], [], []    # Задаем матрицы
    for i in range(row_q):
        A.append([0] * row_q)
        F.append([0] * row_q)
        AF.append([0] * row_q)
        AT.append([0] * row_q)

    for i in range(row_q):
        for j in range(row_q):
            A[i][j] = random.randint(-10,10)
            
    print("A")
    print_matrix(A)
    
    for i in range(row_q):
        for j in range(row_q):
            F[i][j] = A[i][j]

    size=row_q//2
    B = []
    submatrix(B)
    for i in range(size):
        for j in range(size):
            B[i][j]=F[i][size+j]
    
    n=0
    for i in range(size):
        for j in range(size//2, size):
            if B[i][j]==0 and j%2==1 and i<j and i+j>size+1:
                n+=1

    sum=0
    for i in range(size):
        for j in range(size//2):
            if B[i][j]>0 and i%2==1 and i>j and i+j<size-1:
                sum+=B[i][j]

    C = []
    submatrix(C)
    for i in range(size):
        for j in range(size):
            C[i][j]=F[size+i][size+j]
            
    if n>sum:
        for i in range(size):
            for j in range(size):
                if (i == 0) and (j < size - 1 - i) and (j > 0):
                    C[i][j], C[j][size - 1] = C[j][size - 1], C[i][j]
                if (i < j) and (j < size - 1 - i) and (i > 0):
                    C[i][j], C[j][size - 1 - i] = C[j][size - 1 - i], C[i][j]
    for i in range(size):
        for j in range(size):
            C[i][j]=F[size+i][size+j]
    else:
        for i in range(size):
            for j in range(size):
                F[size+i][size+j],F[i][j] = F[i][j],F[size+i][size+j]
    
    print("F")
    print_matrix(F)
    
    for i in range(row_q):  # K*F
        for j in range(row_q):
            F[i][j] = K * F[i][j]
    print("K*F")
    print_matrix(F)

    for i in range(row_q):  # A*(K*F)
        for j in range(row_q):
            s = 0
            for m in range(row_q):
                s = s + A[i][m] * F[m][j]
            AF[i][j] = s
    print("A*(K*F)")
    print_matrix(AF)

    for i in range(row_q):  # A^T
        for j in range(i, row_q, 1):
            AT[i][j], AT[j][i] = A[j][i], A[i][j]
    print("A^T")
    print_matrix(AT)

    for i in range(row_q):  # K*A^T
        for j in range(row_q):
            AT[i][j] = K * AT[i][j]
    print("K*A^T")
    print_matrix(AT)
     
    for i in range(row_q):  # A*(K*F)-(K*A^T)
        for j in range(row_q):
            AF[i][j] = AF[i][j] - AT[i][j]
    print("A*(K*F)-(K*A^T)")
    print_matrix(AF)
    
    print("A")
    print_matrix(A)
    
    finish = time.time()
    result = finish - start
    print("\nProgram time: "+ str(result) +" seconds.")
    print("Program size: "+ str(os.path.getsize('lab-4.py')) +" bytes.")

except ValueError:
    print("\n это не число") 

except FileNotFoundError:
    print("\n файл не найден")
