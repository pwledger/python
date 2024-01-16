# 반복 for

# 리스트 , 튜플 , 문자열의 값을 차례대로 가져 올때 사용
arr = [1,6,10,20,-1]
for 변수 in arr:
    print(변수)
    if 변수 == 10:
        break
        
# 숫자의 범의를  반복 할 때 
for i in range(1,10,2):  # range(시작 , 끝)
    print(i , end = " ")
    
print("\n---range 형태---")
a = list( range(1,5) ) # [1, 2, 3, 4]
print(a)
b = list( range(1,10,2) )  # [1, 3, 5, 7, 9]
print(b)
c = list( range(3) ) # [0,1,2]
print(c)