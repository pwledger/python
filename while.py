# while : 특정 조건일때 계속 반복
a = 0
while True:
    print(a,"안녕")
    a += 1
    if a == 10:
        break

# 10 부터 20 까지 숫자를 차례대로 출력하도록 만들어 보시오
a = 10
while a < 21:
    print(a , end = " ")
    a += 1
    

안내사항 = """
--------------
1.리스트 추가 
2.리스트 삭제
3.리스트 출력
4.종류
--------------
"""
arr = []
while True:
    print(안내사항)
    a = int(input("원하는 번호를 입력하시오 : "))
    if a == 1:
        arr.append(10)
    if a == 2: 
        del arr[0]
    if a == 3:
        print(arr)
    if a == 4:
        break
    