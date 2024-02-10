# 변수 선언, 입력
arr = map(int, input().split())
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
if b > a and c > b:
	print(1)
else:
	print(0)