rows = int(input("Enter Rows"))
colmns = int(input("Enter Columns"))
print (("Rows are {}, columns are {}").format(rows,colmns))
mat = list()
for i in range (0,rows):
    mat.append([])
    for j in range (0,colmns):
        mat[i].append(j)
        print ("Entry in row: ", i+1, " column: ", j+1)
        mat[i][j] = int (input())
print (mat)
