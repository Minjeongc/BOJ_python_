import sys
test_case = int(input())

word = []
for _ in range(test_case):
    temp = sys.stdin.readline().rstrip('\n')
    if temp not in word:
            word.append(temp)

word.sort()
word.sort(key = len)

for i in word:
    print(i)

# 리스트 검색: 검색할 대상 in 리스트
# 문자열 검색: 문자열.find(검색할 대상)
#sort (key= ?) : 검색하기