import math 
afternoon , night , height = map(int, input().split())


temp = afternoon - night

num = (height - night ) / temp

print( math.ceil(num))
