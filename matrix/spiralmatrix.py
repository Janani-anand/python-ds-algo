def spiralmatrix(matrix):
    row1=0
    col1=0
    res=[]
    row=len(matrix)-1
    col=len(matrix[0])-1

    while row1<=row and col1<=col:
        for c in range(col1,col+1):
            res.append(matrix[row1][c])
        row1=row1+1

        for r in range(row1,row+1):
            res.append(matrix[r][col])
        col=col-1

        if(row1<=row):
            for c in reversed(range(col1,col+1)):
                res.append(matrix[row][c])
            row=row-1

        if(col1<=col):
            for r in reversed(range(row1,row+1)):
                res.append(matrix[r][col1])
            col1=col1+1
    return res

if __name__=='__main__':
    a = [ [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18] ]
    print(*spiralmatrix(a),sep=" ")
