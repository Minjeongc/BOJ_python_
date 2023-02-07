# num1, num2 = input().split()

# re_num1 = ''
# re_num2 = ''

# for i in reversed(num1):
#     re_num1 = re_num1 + i 
# for i in reversed(num2):
#     re_num2 = re_num2 + i 

# result = str(int(re_num1) + int(re_num2))

# for i in range(len(result)):
#     if i == 0 and result[-1-i] == '0':
#         continue
#     else:
#         print(result[-1-i], end = "")
x, y = map(str, input().split())
s = str(int(x[::-1]) + int(y[::-1]))
print(int(s[::-1]))        