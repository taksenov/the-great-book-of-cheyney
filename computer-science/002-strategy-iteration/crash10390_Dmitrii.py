#Создаем первый список
list = ['Asp','Carp','Ide','Trout'] 
#Создаем второй список
list2 = ['Cod','Herring','Marlin']
#Создаем третий пустой список
list3 = []
#Добовляем услоиве пока длина списка первого и второго не будет равно нулю
while not (len(list) and len(list2)) == 0:
    #print(list2)
    # Если первый элемент первого списка больше первого элемента второго списка
    if list[0]>list2[0]:
        #cond = list[0]>list2[0]
        #print(cond)
        #Создать переменную рыба и поместить в нее значение равную первому элементу первого списка удалив ее из списка
        fish=list.remove(0)
        #print(fish)
       #fish=list2.remove[0]
       #print(fish)
        #list.remove(0)
        #delete=list.remove(0)
        #print(delete)
        #i+=1
        #print(list3)
    #Иначе
    else:
        #Переменной рыба дать значение удаленное из втрого списка
        fish=list2.remove(0)
        # Списку 3 добавить значение переменной рыба
        list3.append(fish)
        #Вывесте на экран
        print(*list3, sep="\n", end="\n\n") 



#1 написать список с морскими +
#2 написать список с пресными +
#3 создать пустой список +
#4 написать условия что пока списки не пусты +
#6 брать значение из морского сравнивать с пресным если больше удалять из списка
#7 иначе значение из пресного списка удалять
#8 добовлять в новый список
#9 выдать спискок 










#list = ['Asp','Carp','Ide','Trout']
#list2 = ['Cod','Herring','Marlin']
##i = j = 0
#list3 = []
#while not (len(list) and len(list2))==0:
#    if list[0]<list2[0]:
#        list3.append(list[0])
#    else:
#        list3.append(list2[0])
#print(*list3, sep="\n", end="\n\n")


#list = ['Asp','Carp','Ide','Trout']
#list2 = ['Cod','Herring','Marlin']
#def merge_two_list(list, list2):
#    list3 = []
#    i = j = 0
#    while not len(list)==0 and len(list2)==0:
#        if list[i]>list2[j]:
#            list3.append(list[i])
#            i+=1
#        else:
#            list3.append(list2[j])
#            j+=1
#        result.append(list3)
#    print(*list3, sep="\n", end="\n\n")