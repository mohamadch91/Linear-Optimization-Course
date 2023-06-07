for i in range(1,8):
    for j in range(5):
        print("x"+str((i+j)%7+1),end=" ")
    print(">=T"+str((i+4)%7+1),end=" ")
    print("")