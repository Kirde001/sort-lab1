import random
import time
print('Выбор сортировки: 1 - вставками, 2 - выбором')
p = int(input())
a = []
b = []
n = 10000
while len(a) < n:
    korneev = (random.randint(-(n*10),(n*10))) #создание в одну строчку не такое интересное
    if korneev not in a:
        a.append(korneev)
while len(b) < n:
    korneev = (random.randint(-(n*10),(n*10)))
    if korneev not in b:
        b.append(korneev)
yar = set(a)
goga = set(b)
HOO = list(yar) #тут можно было приравнять напрямую к массивам а и б, но сеты чутка перемешивают, поэтому почему бы и нет
KORN = list(goga)
KIR = list(yar.union(goga))
if p == 1:
    def insertion_sort(arr):
        st = time.time()
        swap = comp = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while (j >=0) and (key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
                swap +=1
                comp +=1
            if (j>=0) == False: #пассуем на одном из ненужных условий выхода, ниже нужное
                pass
            elif (key < arr[j]) == False: #условие на выход из вайла
                comp +=1
            arr[j+1] = key
        print(arr)
        print('Объединение массивов. Время работы сортировки - ', time.time() - st)
        print('Количество перестановок - ', swap , ', количество сравнений - ', comp )
        print('\n')
    insertion_sort(HOO)
    insertion_sort(KORN)
    insertion_sort(KIR)
elif p == 2:
    def choicesort(B):
        st = time.time()
        swap = comp = 0
        for i in range (len(B)-1):
            min_ind = i
            swap +=1
            for k in range(i+1,len(B)):
                comp+=1
                if int(B[k]) < int(B[min_ind]):
                    min_ind = k
            B[i],B[min_ind] = B[min_ind],B[i]
        print(B)
        print('Объединение массивов. Время работы сортировки - ', time.time() - st)
        print('Количество перестановок - ', swap, ', количество сравнений - ', comp)
        print('\n')
    choicesort(HOO)
    choicesort(KORN)
    choicesort(KIR)
