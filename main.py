def myfunction (n):
    for i in range(0,n+1):
        print("First Loop")
    j = 1

    while(j<=n+1):
        print("Second Loop",j)
        j = j*2
    for i in range(0,100):
        print("Third loop")
print(myfunction(1))
print("The first loop takes 2 seconds.")
print("The second loop takes 8 seconds")
print("The third loop takes  a lot of time")