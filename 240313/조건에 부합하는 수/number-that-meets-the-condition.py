a = int(input())

condition_list =[] 

for i in range(1, a+1):
    condition_list.append(i)
    if (i%2==0 and i%4!=0) or (i//8)%2==0 or i%7 < 4:
            condition_list.remove(i)
            
for i in condition_list:
    print(i, end=' ')