# x = 10
# for i in range(x):
#     for a in range(i+1):
#         print(" ", end=" ")
#     for j in range(x-i):
#         print("*", end=" ")
#     for q in range(x-i-1):
#         print("*", end=" ")
#     print("")

x = 10
for i in range(x):
    for a in range(x-i):
        print(" ", end=" ")
    for b in range(i):
        for e in range(b-1):
            print("^", end=" ")
        print("*", end=" ")
    for b in range(i+1):
        print("*", end=" ")
    for a in range(x-i):
        print(" ", end=" ")
    
    print("")