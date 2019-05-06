rows = int(input("Enter Rows"))
colmns = int(input("Enter Columns"))
print (("Rows are {}, columns are {}").format(rows,colmns))
mat = []
for i in range (0,rows):       
    mat.append([])
for i in range (0,rows):
    for j in range (0,colmns):
        mat[i].append(j)
        mat[i][j] = 0
print (mat)
for i in range (0,rows):
    for j in range (0,colmns):
        print ("Entry in row: ", i+1, " column: ", j+1)
        mat[i][j] = int (input())
print (mat)
