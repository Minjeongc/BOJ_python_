from collections import deque
import sys
input = sys.stdin.readline
while True:
    flag = True
    temp = input().rstrip('\n')
    result = deque([])
    if temp == '.':
        exit()
    else: 
        for i in temp:
            if (i == '[' or i == '('):
                result.append(i)
            elif (i == ']' or i == ')'):
                if len(result) == 0 :
                    flag = False
                    break
                elif i == ']' and result[-1] == '[':
                    result.pop()
                elif i == ')' and result[-1] == '(' :
                    result.pop()
                else:
                    flag = False
                    break
        if result or flag == False:
            print("no")
        else:
            print("yes")

            #       if result :
            #         if result[-1] == '[':
            #             result.pop()
            #         else:
            #             flag = False 
            #     else:
            #         flag = False
            #         break
            # elif ( i == ')'):
            #     if result: 
            #         if result[-1] == '(':
            #             result.pop()
            #     else:
            #         flag = False 
            #         break          
                          

