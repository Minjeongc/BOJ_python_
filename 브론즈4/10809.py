S = input()

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = [-1]*26
m=0
for i in range(0,26):
        n = alpha[i]
        print(type(n))
        if (num[i] == -1):
                num[i] = (S.find(n))
        # print(n, i)
        
        
for j in num:
        print(j)