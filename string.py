# 문자열 자세한 설명
s = "안녕하세요 반갑습니다"
#    0 1 2345 6 78 910
# indexing 인덱싱 (순서 또는 가리키는 것)
print(s)
print(s[0] , s[1] , s[6])

# 슬라이싱
print(s[0:7]) # 0 부터 시작해서 7 보다 하나 작은 곳 까지

s1 = "123456"
print(s1[0:5:2]) # 1 부터 5 전까지 2간격으로

print(s1[::-1])  # 뒤집기 

a1 = "hello sumin"
a1 = a1.replace('sumin' , 'minsu')
print(a1)
print(len(a1))