l = [[1,2,3],[2,3,1,1]]
for i in range(len(l)):
    for n in range(len(l[i])):
        if l[i][n] == '1':
            l[i][n] = 0

print(l)
 



