            #
        #       #
    #       #       #
#       #       #       #
for row in range(1,5):
    for sp in range(1,5-row):
        print(end=" ")
    for col in range(1,row+1):
        print("# ",end="")
    print()
