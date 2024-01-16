# 반복문 구조 문제
# 1번 5,6,7,8,9 가 차례대로 출력하기 (for 과 range 사용)
for i in range(5,10):
    print(i)
# 2번 5,6,7,8,9 의 합을 구하시오 (a += 1)
a = 0
for i in range(5,10):
    a += i
print(a)

# 3번 arr = [6,10,-3,1,2,1,1,4] 있을 때 5 보다 작은 숫자의 개수를 구하시오. (for)
arr = [6,10,-3,1,2,1,1,4]
c = 0
for i in arr:
    if i < 5:
        c += 1
print(c)

# 4번 구구단 만들기 
for a in range(1,10):
    #a = 1
    for i in range(1,10):
        print(f"{a} x {i} = {a*i}" , end = " ")
    print()
