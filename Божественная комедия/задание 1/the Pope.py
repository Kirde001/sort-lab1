import time
import random
print('Выбор сортировки: 1 - вставками, 2 - выбором')
p = int(input())
def OpenSesame(arr,name):
    with open (f'{name}.txt','w+') as lock:
        for i in range(len(arr)):
            if i < (len(arr))-1:
                lock.write(str(arr[i])+'\n')
            else:
                lock.write(str(arr[i]))
        lock.close()
def OpenTheBook(page):
    with open (f'{page}.txt','r') as book:
        newarr = book.read().split('\n')
        book.close
    return newarr
MrDuck = OpenTheBook('text')
Vai = OpenTheBook('text2')
tag = set()
goga = set()
for elem in MrDuck: 
    newel = int(elem) 
    tag.add(newel)
for elem2 in Vai:
    NEWel = int(elem2)
    goga.add(NEWel)
KIR = list(tag.union(goga))
IGA = list(tag.intersection(goga))
SAB = list(tag.difference(goga))
ALE = list(tag.symmetric_difference(goga))
OpenSesame(KIR,'Объединение')
OpenSesame(IGA,'Перечисление')
OpenSesame(SAB,'Разность')
OpenSesame(ALE,'СимметричнаяРазность')
Q = []
W = []
E = []
R = []

######################################################################

if p == 1:
    def insertion_sort(arr,name1,name2):
        st = time.time()
        arr = OpenTheBook(name1) #чтение внутри
        swap = comp = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while (j >=0 and (key < arr[j])):
                arr[j+1] = arr[j]
                j -= 1
                swap +=1
                comp +=1
            if (j >=0) == False:
                pass
            elif (key < arr[j]) == False:
                comp +=1
            arr[j+1] = key
        OpenSesame(arr,name2) #запись в новый файл с припиской РЕЗ
        print(f'{name1} : время работы сортировки - ', time.time() - st)
        print('Количество перестановок - ', swap, ', количество сравнений - ', comp)
        print('\n')
    insertion_sort(Q,'Объединение','ОбъединениеРЕЗ') #записи внутри
    insertion_sort(W,'Перечисление','ПеречислениеРЕЗ')
    insertion_sort(E,'Разность','РазностьРЕЗ')
    insertion_sort(R,'СимметричнаяРазность','СимметричнаяРазностьРЕЗ')


#######################################################################

elif p == 2:
    def choicesort(B,name1,name2):
        st = time.time()
        B = OpenTheBook(name1) #чтение внутри
        swap = comp = 0
        for i in range (len(B)-1):
            min_ind = i
            swap+=1
            for k in range(i+1,len(B)):
                comp+=1
                if int(B[k]) < int(B[min_ind]):
                    min_ind = k
            B[i],B[min_ind] = B[min_ind],B[i] 
        OpenSesame(B,name2) #запись в новый файл с припиской РЕЗ
        print(f'{name1} : время работы сортировки - ', time.time() - st)
        print('Количество перестановок - ', swap , ', количество сравнений - ', comp)
        print('\n')
    choicesort(Q,'Объединение','ОбъединениеРЕЗ')
    choicesort(W,'Перечисление','ПеречислениеРЕЗ')
    choicesort(E,'Разность','РазностьРЕЗ')
    choicesort(R,'СимметричнаяРазность','СимметричнаяРазностьРЕЗ')

#######################################################################

