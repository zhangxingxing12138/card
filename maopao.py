def bubble_sort(num_list): 
    for j in range(len(num_list)-1,0,-1):
        for i in range(j):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
 
li = [12,45,68,32,670978,123,456,76]
bubble_sort(li)
print(li)

