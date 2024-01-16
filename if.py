# 부등호 
print(10 == 10)
print(10 != 9)
print(10 > 5)
print(5 < 10)
print(10 >= 10)
print(10 <= 10)

money = 10000
card = True
if money > 5000 and card:
    print("오늘은 내가 쏜다")
    
card = False
if money > 5000 or card:
    print("오늘도 내가 쏜다")
    
if not card:
    print("카드가 없다")
    
if 1 in [1,4,10]:
    print("1이 [1,4,10] 안에 있다")

if 5 not in [1,4,10]:
    print("5가 [1,4,10] 안에 없다")

a = 10    
if a < 100:
    print(1)
elif a > 60:
    print(2)
else :
    print(3)
    
# 간단한 조건 미션
arr = [1,6,10,35]
# 위 arr 리스트의 합이 50 보다 크면 "50보다 크다" ,50 이하이면 "50 이하이다"
if sum(arr) > 50:
    print("50보다 크다")
elif sum(arr) <= 50:
    print("50이하 이다")

import random
a = random.randint(-10,10)  # -10 ,10 사이 숫자

# a 가 "양수"인지 , "음수"인지 , "0" 인지 알려주세요 
if a > 0:
    print("양수")
elif a < 10:
    print("음수")
else:
    print("0")
