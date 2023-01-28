if __name__ =="__main__":
    sound = list(map(int, input().split()))
    asc = 0
    dec = 0 

    for i in range(len(sound)-1):
        if sound[i] < sound[i+1]:
            asc +=1
        if sound[i] > sound[i+1]:
            dec += 1


    if asc == 7:
        print("ascending")
    elif dec == 7:
        print("descending")
    else:
        print("mixed")
