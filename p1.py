# 리스트 연습 및 조건
# 1 번. arr 이름의 빈 리스트를 만드시오
arr = []
# 2 번. arr 안에 10 , 20 , 30 , 40 , 50 , -10 , 0 , 1, 3 추가 (extend)

# 3 번. arr 오름차순으로 정렬하시오 (sort)

# 4 번. 오름차순으로 정렬한 상태에서 가장 큰수와 가장 작은수의 차이를 구하시오

# 5 번. arr의 평균 값이 50 보다 크면 "통과" , 아니면 "재시험" 이라고 출력하시오

# 6 번. arr의 평균 값이 30 보다 작고 그리고(and) 가장큰수가 60 미만이면 "면담" 그렇지 않으면 "통과" 출력하시오

# 1번
arr =[]
print(arr)
# 2번
arr.extend([10 , 20 , 30 , 40 , 50 , -10 , 0 , 1, 3])
print(arr)
# 3번
arr.sort()
print(arr)
# 4번
print(arr[8] - arr[0]) 
print(max(arr) - min(arr))
print(arr[-1] - arr[0])
# 평균
a = sum(arr)/len(arr)
if a > 50:
    print("통과")
else:
    print("재시험")
# 6번 
if a < 30 and max(arr) < 60 :
    print("면담")
else:
    print("통과")
    