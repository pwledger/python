arr = [1,6,10,20,7,-5]
#순서   0 1 2  3  4  5
print(arr[0]+arr[4])

#바꿀수 있다
s = ["s","u", "m" ,"i" , "n"]
s[0] ="S"
print(s)

# 리스트에는 여러가지 함수
a = [5,7,10]

# 추가 append()
a.append(8)
print(a)   # [5,7,10,8]

# 삭제 del
del a[0]
print(a)   # [7,10,8]

# 개수 len()
print(len(a)) # 3

# 정렬
a.sort()
print(a)   # [7,8,10]

# 기타 sum() , max() , min()
print(sum(a) , max(a) , min(a))