n = int(input())

clean_class_cnt = 0
clean_boc_cnt = 0
clean_bath_cnt= 0

for i in range(1, n+1):
    if i % 12 ==0:
        clean_bath_cnt += 1
    elif i % 3 ==0:
        clean_boc_cnt += 1
    elif i % 2 == 0:
        clean_class_cnt += 1


print(clean_class_cnt, clean_boc_cnt, clean_bath_cnt)