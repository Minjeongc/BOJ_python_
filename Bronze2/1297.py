from math import *
d, h , w= map(int, input().split())

x = pow(d,2) / (pow(h,2) + pow(w,2))

x = sqrt(x)

height = h* x
weight = w * x
print(floor(height), floor(weight))
