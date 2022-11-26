n, m = 4,3
list = ['Asp','Carp','Ide','Trout']
list2 = ['Cod','Herring','Marlin']
i = j = 0
list3 = []
while i<n and j<m:
    if list[i]<list2[j]:
        list3.append(list[i])
        i+=1
    else:
        list3.append(list2[j])
        j+=1
while i<n:
        list3.append(list[i])
        i+=1
print(*list3, sep="\n", end="\n\n") 
