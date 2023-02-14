while True:
    s = input()
    if s == '# 0 0':
        break
    name, year, weight = s.split()
    year = int(year)
    weight = int(weight)
    
    if (year> 17) or (weight>=80):
        print(name + ' Senior')
    else:
        print(name + ' Junior')

