numIn = int(input("Enter number: "))
def collatz(numIn):
    seed = [numIn]
#    print(numIn)

    for i in seed:
        if numIn%2 == 0:
            numIn = numIn/2#computation if number in sequence is even
            seed.append(numIn)
        elif numIn%2 == 1:
            numIn = (numIn * 3) + 1#computation if number in sequence is odd
            seed.append(numIn)#adds next number in the sequence on the end of the list
        if numIn == 1:
            break
    return seed

def length(max):
    seed = 0
    lst = []
    while (seed < max):
        seed = seed + 1
        lst.append(len(collatz(seed)))

    return lst

maxSeed = (max(enumerate(length(numIn)), key = lambda x:x[1]))
print(collatz(maxSeed[0]))
print((max(enumerate(length(numIn)), key = lambda x:x[1])))
#which seed less than a million gives longest sequence and how long is that sequence



#longest
#how long is it?
#what was the seed   #############
#print(max(enumerate(collatz(numIn)), key = lambda x:x[1]))


