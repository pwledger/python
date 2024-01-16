# 리스트 규칙에 대해
arr = [1,6,10,20,7,-5]
#      0 1  2  3 4  5  인덱스 번호

# 문자열 처럼 인데싱 , 슬라이싱이 가능
print(arr[3] , arr[1:4])


# 문자열과 차이 (값을 쉽게 바꿀수 있다)
s = ["h","e","l","l","o"]
s[0] = "H"
print(s)

# 리스트 함수 
a = len(arr) # 리스트의 개수
print(a)

# 추가 
arr.append(100)
print(arr) # [1, 6, 10, 20, 7, -5, 100]
arr.append([200,300]) # [1, 6, 10, 20, 7, -5, 100, [200, 300]]
print(arr , arr[7][0])
# 삭제
del arr[1] # 원하는 번호 삭제
print(arr) # 1, 10, 20, 7, -5, 100, [200, 300]]
arr.pop()  # 맨뒤에 있는거 내보내면서 삭제 
print(arr) # 1, 10, 20, 7, -5, 100

# 정렬
arr.sort()  # 오름차순 ( 작은수 >> 큰수 )
print(arr)
arr.sort(reverse = True) # 내림차순 (큰수 >> 작은수 )
print(arr) 

# 합 ,평균 , 가장큰수 , 가장작은수 
print(sum(arr) , sum(arr)/len(arr), max(arr), min(arr))