# test_case = int(input())
# result = 0
# for _ in range(test_case):
#     word = input()
#     for i in range(len(word)-1):
#         if word[i] != word[i+1] :
#             pass
#         elif word[i] in word[i+1:]:
#             result += 1
#             break

# print(result)

N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)