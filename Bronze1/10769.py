n = input()

cnt1 = n.count(":-)")
cnt2 = n.count(":-(")


if cnt1 == 0 and cnt2 == 0:
    print("none")
elif cnt1 == cnt2 :
    print("unsure")
elif cnt1 > cnt2:
    print("happy")
elif cnt1 < cnt2 : 
    print("sad")