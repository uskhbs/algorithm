# 문자열 뒤집기
# 전부 0으로 바꾸기 and 전부 1로 바꾸기

s = input()

count0 = 0
count1 = 0

if s[0] == '1' :
    count0 += 1
else :
    count1 += 1

for i in range(len(s)-1) :
    if s[i] != s[i+1] :
        if s[i+1] == '1' :
            count0 += 1
        else :
            count1 += 1
            
print(min(count0 , count1))