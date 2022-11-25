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
#print(*list3)





#def merge (list, list2):
#    result = []
#list3=[list + list2]
##print (list3)
#while not [list and list2]:
#    if list[0] > list2[0]:
#        list3 == list.remove[0]
##        print (list3)
#    else:
#        list3 == list2.remove[0]
#        result.append (list3)
##    else:
##        list3 == list2.pop(0)
#print (*list3)


#while not (list.empty and list2.empty)
# if list.top_item>list2.top_item
# else
#    list = list.remove_top_item
#result.append(fish)
#return result
#print (list3)
