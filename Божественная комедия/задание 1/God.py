import random
kk = open ("text.txt",'w+')
a = []
n = 5000
while len(a) < n:
    korneev = (random.randint(-(n*10),(n*10)))
    if len(a) < n-1 :
        if korneev not in a:
            a.append(korneev)
            kk.write(str(korneev)+'\n')
    else:
        if korneev not in a:
            a.append(korneev)
            kk.write(str(korneev))
kk.close()
kk = open ("text2.txt",'w+')
a = []
while len(a) < n:
    korneev = (random.randint(-(n*10),(n*10)))
    if len(a) < n-1:
        if korneev not in a:
            a.append(korneev)
            kk.write(str(korneev)+'\n')
    else:
        if korneev not in a:
            a.append(korneev)
            kk.write(str(korneev))
kk.close()
print('This is the beginning of the end')
######################################################
with open('text.txt','r+') as kk:
    A = kk.read().split('\n')
    def AdamFatherOfTheMankind():
        for i in range (len(A)-1):
            min_ind = i
            for k in range(i+1,len(A)):
                if int(A[k]) < int(A[min_ind]):
                    min_ind = k
            A[i],A[min_ind] = A[min_ind],A[i]
    AdamFatherOfTheMankind()
with open('text.txt','w+') as gg:
    for i in range(len(A)):
       if i < (len(A)-1):
            gg.write(str(A[i])+'\n')
       else:
           gg.write(str(A[i]))
    print('This was your fault')
#######################################################
with open ("text2.txt") as kk:
    arr = kk.read().split('\n')
    def EveTheFirstWoman():
        for i in range(1, len(arr)):
            key = int(arr[i])
            j = i-1
            while j >=0 and key < int(arr[j]) :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    EveTheFirstWoman()
with open('text2.txt','w+') as gg:
    for i in range(len(arr)):
        if i < len(arr)-1:
            gg.write(str(arr[i])+'\n')
        else:
            gg.write(str(arr[i]))
