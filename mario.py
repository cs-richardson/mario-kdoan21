#program that recreates the half-pyramid in Mario using hashes (#) for blocks.

pyramidHeight = int(input("Height(1-23): "))

if pyramidHeight < 0 or pyramidHeight > 23:
    print("Invalid Input!")
    pyramidHeight = int(input("Height(1-23): "))
else:
    pyramidLayer = pyramidHeight - (pyramidHeight - 2)
    pyramidCheck = 0
    
    while pyramidCheck != pyramidHeight:
            print("#" * pyramidLayer)
            pyramidLayer = pyramidLayer + 1
            pyramidCheck = pyramidCheck + 1
