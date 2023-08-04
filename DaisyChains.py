flowers = int(input())
input1 = input()
flowers_petals = [int(i) for i in input1.split()]


#flowers = 4
#flowers_petals = [1,1,2,3]
count = 0

i = 0
while i < flowers:
    for x in range(i+1,flowers+1):
        if sum(flowers_petals[i:x])/len(flowers_petals[i:x]) in flowers_petals[i:x]:
            count += 1
    i += 1
print(count)   


    
