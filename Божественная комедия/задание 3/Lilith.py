import random
import time
print('Выбор сортировки: 1 - вставками, 2 - выбором')
p = int(input())
a = []
b = []
n = 1000
while len(b) < n:
    while len(a) < n:
        korn = random.randint(-(n*10),(n*10))
        a.append(korn)
    b.append(a)
    a = []
if p ==1:
    def insertion_sort(b):
        st = time.time()
        swap = comp = 0
        for q in range(len(b)): #строки
            for i in range(1, len(b)):
                key = b[q][i]
                j = i-1
                while (j >=0) and (key < b[q][j]) :
                    b[q][j+1] = b[q][j]
                    j -= 1
                    swap +=1
                    comp +=1
                if (j>=0) == False:
                    pass
                elif (key < b[q][j]) == False:
                    comp+=1
                b[q][j+1] = key
        for q in range(len(b)):
            for i in range(1, len(b)): #столбцы
                key = b[i][q]
                j = i-1
                while (j >=0) and (key < b[j][q]):
                    b[j+1][q] = b[j][q]
                    j -= 1
                    swap +=1
                    comp +=1
                if (j>=0) == False:
                    pass
                elif (key < b[j][q]) == False:
                    comp+=1
                b[j+1][q] = key
        print('Время работы сортировки - ', time.time() - st)
        print('Количество перестановок - ', swap, ', количество сравнений - ', comp)
        print('\n')
    insertion_sort(b)
elif p == 2:
    def choicesort(b):
        st = time.time()
        swap = comp = 0
        for k in range(len(b)):
            for p in range(len(b)-1): #строки
                min_i = p
                swap +=1
                for y in range(p+1,len(b)):
                    comp +=1
                    if b[k][y] < b[k][min_i]:
                        min_i = y
                b[k][p],b[k][min_i] = b[k][min_i],b[k][p]
        for k in range(len(b)):
            for r in range(len(b)-1): #столбцы
                min_ind = r 
                swap +=1
                for o in range(r+1,len(b)):
                    comp +=1
                    if b[o][k] < b[min_ind][k]:
                        min_ind = o
                b[r][k],b[min_ind][k] = b[min_ind][k],b[r][k]
        print('Время работы сортировки - ', time.time()-st)
        print('Количество перестановок - ', swap, ', количество сравнений - ', comp)
        print('\n')
    choicesort(b)
print(b)
