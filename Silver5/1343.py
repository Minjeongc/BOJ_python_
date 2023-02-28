# word = input()
# cnt = 0
# temp = []
# ans = []
# flag = True
# for i in word:
#     if i == 'X':
#         cnt += 1
#     elif i == '.' :
#         temp.append(cnt)
#         temp.append('.')
#         cnt = 0
# temp.append(cnt)

# for i in temp:
#     if i == '.':
#         ans.append('.')
#         continue
#     while i > 0 :
#         if i - 4 >= 0:
#             ans.append('AAAA')
#             i = i - 4
#         elif i - 2 >= 0:
#             ans.append('BB')
#             i = i - 2
#         else:
#             if i % 2 == 1:
#                 flag = False
#                 print(-1)
#                 break

# if flag:
#     for i in ans:
#         print(i, end = "")

word = input()

word = word.replace("XXXX","AAAA")
word = word.replace("XX", "BB")

if 'X' in word:
    print(-1)
else:
    print(word)